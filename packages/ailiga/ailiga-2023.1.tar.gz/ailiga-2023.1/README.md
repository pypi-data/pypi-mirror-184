# AILiga

[![Documentation Status](https://readthedocs.org/projects/ailiga/badge/?version=latest)](https://ailiga.readthedocs.io/en/latest/?badge=latest)

## Goals

* Monthly releases of session/tournament results
* User folders
* Strict versioning for reproducibility (ocne a version is pushed, gitignore it)

## Installation

```sh
git clone THIS_PROJECT_URL
poerty install
poetry shell
```




## Testing and Training

Currently, training/testing fighters works through the fighter tests.
```sh
python tests/test_dqn_fighter.py
```

## Tensorboard

```sh
tensorboard --logdir log/ --load_fast=false
```


## Limitations

Currently, the implementation through `tianshou.BasePolicy` seems to only support DQNPolicy and also not `Discrete()` observation spaces.

## References

### Frameworks

* https://github.com/Farama-Foundation/PettingZoo
* https://github.com/vwxyzjn/cleanrl
* https://github.com/Farama-Foundation/Gymnasium
* https://github.com/deepmind/open_spiel
* https://github.com/datamllab/rlcard
* https://tianshou.readthedocs.io/en/master/

### Books

* http://incompleteideas.net/book/the-book-2nd.html


## Development

We use black through

### package/python structure:

* https://mathspp.com/blog/how-to-create-a-python-package-in-2022
* https://www.brainsorting.com/posts/publish-a-package-on-pypi-using-poetry/
