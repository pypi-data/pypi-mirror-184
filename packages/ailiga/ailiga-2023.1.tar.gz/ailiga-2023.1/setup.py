# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ailiga',
 'ailiga.APNPucky.DQNFighter.v0',
 'ailiga.APNPucky.DQNFighter.v1',
 'ailiga.APNPucky.DQNFighter.v2',
 'ailiga.APNPucky.DRDQNFighter',
 'ailiga.APNPucky.PPOFighter',
 'ailiga.APNPucky.RandomFigher.v0']

package_data = \
{'': ['*'],
 'ailiga.APNPucky.DQNFighter.v0': ['knights_archers_zombies_v10/*',
                                   'leduc_holdem_v4/*',
                                   'simple_spread_v2/*',
                                   'simple_spread_v2/APN-Pucky/*',
                                   'tictactoe_v3/*',
                                   'tictactoe_v3/APN-Pucky/*'],
 'ailiga.APNPucky.DQNFighter.v1': ['knights_archers_zombies_v10/*',
                                   'leduc_holdem_v4/*',
                                   'simple_spread_v2/*',
                                   'simple_spread_v2/APN-Pucky/*',
                                   'tictactoe_v3/*',
                                   'tictactoe_v3/APN-Pucky/*'],
 'ailiga.APNPucky.DQNFighter.v2': ['knights_archers_zombies_v10/*',
                                   'leduc_holdem_v4/*',
                                   'simple_spread_v2/*',
                                   'simple_spread_v2/APN-Pucky/*',
                                   'tictactoe_v3/*',
                                   'tictactoe_v3/APN-Pucky/*']}

install_requires = \
['PettingZoo<1.22.0',
 'SuperSuit',
 'cfg_load',
 'h5py',
 'pqdm',
 'pygame',
 'pyglet==1.5.27',
 'rlcard',
 'smpl_doc>=1.1.1',
 'smpl_io',
 'tianshou==0.4.10',
 'torch==1.13.0',
 'tqdm']

entry_points = \
{'console_scripts': ['ailiga-tournament = ailiga.tournament:main',
                     'ailiga-train = ailiga.train:main']}

setup_kwargs = {
    'name': 'ailiga',
    'version': '2023.1',
    'description': '',
    'long_description': '# AILiga\n\n[![Documentation Status](https://readthedocs.org/projects/ailiga/badge/?version=latest)](https://ailiga.readthedocs.io/en/latest/?badge=latest)\n\n## Goals\n\n* Monthly releases of session/tournament results\n* User folders\n* Strict versioning for reproducibility (ocne a version is pushed, gitignore it)\n\n## Installation\n\n```sh\ngit clone THIS_PROJECT_URL\npoerty install\npoetry shell\n```\n\n\n\n\n## Testing and Training\n\nCurrently, training/testing fighters works through the fighter tests.\n```sh\npython tests/test_dqn_fighter.py\n```\n\n## Tensorboard\n\n```sh\ntensorboard --logdir log/ --load_fast=false\n```\n\n\n## Limitations\n\nCurrently, the implementation through `tianshou.BasePolicy` seems to only support DQNPolicy and also not `Discrete()` observation spaces.\n\n## References\n\n### Frameworks\n\n* https://github.com/Farama-Foundation/PettingZoo\n* https://github.com/vwxyzjn/cleanrl\n* https://github.com/Farama-Foundation/Gymnasium\n* https://github.com/deepmind/open_spiel\n* https://github.com/datamllab/rlcard\n* https://tianshou.readthedocs.io/en/master/\n\n### Books\n\n* http://incompleteideas.net/book/the-book-2nd.html\n\n\n## Development\n\nWe use black through\n\n### package/python structure:\n\n* https://mathspp.com/blog/how-to-create-a-python-package-in-2022\n* https://www.brainsorting.com/posts/publish-a-package-on-pypi-using-poetry/\n',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
