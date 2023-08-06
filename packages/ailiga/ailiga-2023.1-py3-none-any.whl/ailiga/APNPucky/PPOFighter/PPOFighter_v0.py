import os

import gym
import numpy as np
import torch
from pettingzoo.classic import rps_v2, tictactoe_v3
from tianshou.data import Collector, VectorReplayBuffer
from tianshou.env import DummyVectorEnv, PettingZooEnv
from tianshou.env.pettingzoo_env import PettingZooEnv
from tianshou.policy import (
    BasePolicy,
    DQNPolicy,
    MultiAgentPolicyManager,
    PPOPolicy,
    RandomPolicy,
)
from tianshou.trainer import offpolicy_trainer, onpolicy_trainer
from tianshou.utils import TensorboardLogger
from tianshou.utils.net.common import ActorCritic, Net
from tianshou.utils.net.discrete import Actor, Critic
from torch.utils.tensorboard import SummaryWriter

from ailiga.APNPucky.RandomFigher.v0.RandomFighter_v0 import RandomFighter_v0
from ailiga.fighter import Fighter
from ailiga.trained_fighter import TrainedFighter


class PPOFighter_v0(TrainedFighter):
    user = "APN-Pucky"

    # https://tianshou.readthedocs.io/en/master/tutorials/dqn.html
    buffer_size = 20_000

    lr = 3e-4
    gamma = 0.99
    max_grad_norm = 0.5
    eps_clip = 0.2
    vf_coef = 0.5
    ent_coef = 0.0
    gae_lambda = 0.95
    rew_norm = 0
    dual_clip = None
    value_clip = 0
    norm_adv = 0
    recompute_adv = 0

    hidden_sizes = [64, 64]

    reward_threshold = 100

    epoch = 10
    step_per_epoch = 50_000
    repeat_per_collect = 10
    training_num = 20
    test_num = 100
    batch_size = 64
    step_per_collect = 2000

    def compatible_envs(self):
        return ["tictactoe_v3", "CartPole-v0"]

    def __init__(self, lambda_env, savefile=None):
        super().__init__(lambda_env)
        self.env = lambda_env()
        env = self.env
        device = "cuda" if torch.cuda.is_available() else "cpu"
        observation_space = (
            env.observation_space["observation"]
            if isinstance(env.observation_space, gym.spaces.Dict)
            else env.observation_space
        )
        state_shape = observation_space.shape or observation_space.n
        action_shape = env.action_space.shape or env.action_space.n

        if self.reward_threshold is None:
            default_reward_threshold = {"CartPole-v0": 195}
            self.reward_threshold = default_reward_threshold.get(
                env, env.spec.reward_threshold
            )

        net = Net(state_shape, hidden_sizes=self.hidden_sizes, device=device)
        actor = Actor(net, action_shape, device=device).to(device)
        critic = Critic(net, device=device).to(device)
        actor_critic = ActorCritic(actor, critic)
        # orthogonal initialization
        for m in actor_critic.modules():
            if isinstance(m, torch.nn.Linear):
                torch.nn.init.orthogonal_(m.weight)
                torch.nn.init.zeros_(m.bias)
        optim = torch.optim.Adam(actor_critic.parameters(), lr=self.lr)
        dist = torch.distributions.Categorical
        policy = PPOPolicy(
            actor,
            critic,
            optim,
            dist,
            discount_factor=self.gamma,
            max_grad_norm=self.max_grad_norm,
            eps_clip=self.eps_clip,
            vf_coef=self.vf_coef,
            ent_coef=self.ent_coef,
            gae_lambda=self.gae_lambda,
            reward_normalization=self.rew_norm,
            dual_clip=self.dual_clip,
            value_clip=self.value_clip,
            action_space=env.action_space,
            deterministic_eval=True,
            advantage_normalization=self.norm_adv,
            recompute_advantage=self.recompute_adv,
        )
        self.policy = policy
        self.load(savefile)

    def train(self, savefile=None, seed=None, reset=True):
        super().train(seed, reset)

        agents = [
            *[
                RandomFighter_v0(self.lambda_env).get_policy()
                for _ in range(len(self.env.agents) - 1)
            ],
            self.policy,
        ]
        self.agentindex = -1
        policy = MultiAgentPolicyManager(agents, self.env)
        agents = self.env.agents

        # collector
        train_collector = Collector(
            policy,
            self.train_envs,
            VectorReplayBuffer(self.buffer_size, len(self.train_envs)),
        )
        test_collector = Collector(self.policy, self.test_envs)

        def stop_fn(mean_rewards):
            return mean_rewards >= self.reward_threshold

        # trainer
        result = onpolicy_trainer(
            self.policy,
            train_collector,
            test_collector,
            self.epoch,
            self.step_per_epoch,
            self.repeat_per_collect,
            self.test_num,
            self.batch_size,
            step_per_collect=self.step_per_collect,
            stop_fn=stop_fn,
            reward_metric=self.reward_metric,
            save_best_fn=self.save,
            logger=self.get_logger(),
        )
        assert stop_fn(result["best_reward"])
