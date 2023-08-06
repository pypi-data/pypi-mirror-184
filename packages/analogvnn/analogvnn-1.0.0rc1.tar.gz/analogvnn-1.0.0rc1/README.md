# AnalogVNN

[![PyPI version](https://badge.fury.io/py/analogvnn.svg)](https://badge.fury.io/py/analogvnn)
[![Documentation Status](https://readthedocs.org/projects/analogvnn/badge/?version=stable)](https://analogvnn.readthedocs.io/en/stable/?badge=stable)
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL_2.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)

AnalogVNN Paper: [https://arxiv.org/abs/2210.10048](https://arxiv.org/abs/2210.10048)

Documentation: [https://analogvnn.readthedocs.io/](https://analogvnn.readthedocs.io/)

Cite: Vivswan Shah, and Nathan Youngblood. "AnalogVNN: A fully modular framework for modeling and optimizing photonic
neural
networks." *arXiv preprint arXiv:2210.10048 (2022)*.

Installation:
- Install [PyTorch](https://pytorch.org/)
- Install AnanlogVNN using [pip](https://pypi.org/project/analogvnn/)
```bash
pip install analogvnn
```

AnalogVNN is a simulation framework built on PyTorch which can simulate the effects of
optoelectronic noise, limited precision, and signal normalization present in photonic
neural network accelerators. We use this framework to train and optimize linear and
convolutional neural networks with up to 9 layers and ~1.7 million parameters, while
gaining insights into how normalization, activation function, reduced precision, and
noise influence accuracy in analog photonic neural networks. By following the same layer
structure design present in PyTorch, the AnalogVNN framework allows users to convert most
digital neural network models to their analog counterparts with just a few lines of code,
taking full advantage of the open-source optimization, deep learning, and GPU acceleration
libraries available through PyTorch.
