# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scytale_cipher']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['scytale = scytale_cipher.scytale:main']}

setup_kwargs = {
    'name': 'scytale-cipher',
    'version': '0.1.2',
    'description': 'Scytale cipher algorithm cli tool',
    'long_description': '# Scytale\n\nJust a very simple python script to calculate the scytale-cipher through an cli-wizard.\n\nThe projects main purpose is to showcase interesting tooling to build, publish and develop python apps.\n\n## Code Status\n\n[![CI](https://github.com/lockejan/scytale/actions/workflows/branch.yml/badge.svg?branch=main)](https://github.com/lockejan/scytale/actions/workflows/branch.yml)\n[![codecov](https://codecov.io/gh/lockejan/scytale/branch/main/graph/badge.svg?token=IVZBSROEKF)](https://codecov.io/gh/lockejan/scytale)\n\nCode documentation: https://scytale.readthedocs.io\n\n## Description\n\nThe scytale was used more than 2500 years ago by the Spartans, and is one example of ancient cryptography.\nA message gets written on a ribbon which is then wrapped around a stick with a certain diameter (the scytale).\n\nBelow is a sample encryption of the plain text "prove me wrong!" with a scytale of diameter 3.\nWe write the message around the scytale, and then\n\n```\n|p|r|o|\n - - -\n|v|e| |\n - - -\n|m|e| |\n - - -\n|w|r|o|\n - - -\n|n|g|!|\n```\n\nThe cipher text is obtained by reading from top to bottom, left to right.\nIn this example, the cipher text is\n\n```\npvmwnreergo  o!\n```\n\n## Setup\n\n### Using Nix\n\nTo follow this path at least Nix has to be installed (and flakes have to be enabled).\n\n- `nix develop` will drop you into a shell containing everything to further hack on the project.\nInside the devShell invoking `scytale` should bring up a prompt.\n\n- `nix run` will run the default app of the flake file.\n\n- `nix build` will build the default package with the help of [poetry2nix](https://github.com/nix-community/poetry2nix)\n\n- [default.nix](./default.nix) is included to build the package the non-flake way with `nix-build`.\n- [shell.nix](./shell.nix) contains instructions to provide a non-flake shell via `nix-shell`.\n\n### Without Nix\n\nAt least Poetry needs to be installed.\n\n- `poetry run scytale` will activate the poetry environment and execute the script held in [pyproject.toml](./pyproject.toml#L3).\n    If errors are occurring `poetry install` (installs the virtual environment and all given requirements)\n\n- `poetry shell` (activates and enters the virtual environment)\n\n- `poetry run python -m unittest discover` (runs all tests). Alternatively `poetry run python -m pytest tests` to use pytest for test execution.\n',
    'author': 'Jan Schmitt',
    'author_email': 'git@smittie.de',
    'maintainer': 'Jan Schmitt',
    'maintainer_email': 'git@smittie.de',
    'url': 'https://github.com/lockejan/scytale',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
