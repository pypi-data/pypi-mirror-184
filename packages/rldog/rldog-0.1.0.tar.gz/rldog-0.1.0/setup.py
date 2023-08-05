# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rldog',
 'rldog.agents',
 'rldog.agents.DQN_based',
 'rldog.agents.actor_critics',
 'rldog.agents.policy_gradients',
 'rldog.configs',
 'rldog.dataclasses',
 'rldog.examples',
 'rldog.networks',
 'rldog.tools']

package_data = \
{'': ['*']}

install_requires = \
['gym==0.26.2',
 'matplotlib>=3.6.2,<4.0.0',
 'numpy==1.23.5',
 'pytest>=7.2.0,<8.0.0',
 'rich>=13.0.0,<14.0.0',
 'torch==1.13.1']

setup_kwargs = {
    'name': 'rldog',
    'version': '0.1.0',
    'description': 'Core 4 Reinforcement learning algorithms, implemented with very high quality code (think type hints, tests, pep8 etc). Very easy to use with gym or gym-like environments',
    'long_description': "# PyRL\nEnvironment Agnostic RL algorithm implementations using Pytorch. High quality code, typehints, thorough tests, examples.\nAlso uses minibatches correctly, which most public libraries don't implement.\n\n\nSee examples for some, well, examples. Algos implemented:\n\n1. *Deep Q Learning (DQN)* <sub><sup> ([Mnih et al. 2013](https://arxiv.org/pdf/1312.5602.pdf)) </sup></sub>  \n --- UPCOMING ---\n2. *DQN Experience Replay*  <sub><sup> ([Mnih et al. 2013](https://arxiv.org/pdf/1312.5602.pdf)) </sup></sub> \n3. *DQN with Fixed targets* <sub><sup>([Mnih et al. 2013](https://arxiv.org/pdf/1312.5602.pdf)) </sup></sub> \n4. *Double Q Learning (DDQN)* <sub><sup> ([arXiv:1509.06461v3 [cs.LG] 8 Dec 2015](https://arxiv.org/pdf/1509.06461v3.pdf)) </sup></sub>   \n5. REINFORCE <sub><sup> ([Richard S. Sutton et al 1999](https://proceedings.neurips.cc/paper/1999/file/464d828b85b0bed98e80ade0a5c43b0f-Paper.pdf))\n6. Advantage Actor Critic ([arXiv:1611.06256](https://arxiv.org/abs/1611.06256))\n\n3. PPO\n\nWhat i'm happy with\nQuality of the code, thorough tests, majority of functionality, ease of use & versatility\n\nRun tests with: pytest tests",
    'author': 'Charlie',
    'author_email': 'CharlieJackCoding@Gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
