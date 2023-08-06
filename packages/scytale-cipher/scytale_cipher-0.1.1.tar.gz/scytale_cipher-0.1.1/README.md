# Scytale

[![codecov](https://codecov.io/gh/lockejan/scytale/branch/main/graph/badge.svg?token=IVZBSROEKF)](https://codecov.io/gh/lockejan/scytale)

Just a very simple python script to calculate the scytale-cipher through an cli-wizard.

It also includes some tooling to build, publish and develop with Nix and Poetry.

## Description

The scytale was used more than 2500 years ago by the Spartans, and is one example of ancient cryptography.
A message gets written on a ribbon which is then wrapped around a stick with a certain diameter (the scytale).

Below is a sample encryption of the plain text "prove me wrong!" with a scytale of diameter 3.
We write the message around the scytale, and then

```
|p|r|o|
 - - -
|v|e| |
 - - -
|m|e| |
 - - -
|w|r|o|
 - - -
|n|g|!|
```

The cipher text is obtained by reading from top to bottom, left to right.
In this example, the cipher text is

```
pvmwnreergo  o!
```

## Prerequisites And Usage

### Using Nix

To follow this path at least Nix has to be installed (and flakes have to be enabled).

- `nix develop` will drop you into a shell containing everything to further hack on the project.
Inside the devShell invoking `scytale` should bring up a prompt.

- `nix run` will run the default app of the flake file.

- `nix build` will build the default package with the help of [poetry2nix](https://github.com/nix-community/poetry2nix)

- [default.nix](./default.nix) is included to build the package the non-flake way with `nix-build`.
- [shell.nix](./shell.nix) contains instructions to provide a non-flake shell via `nix-shell`.

### Without Nix

At least Poetry needs to be installed.

- `poetry run scytale` will activate the poetry environment and execute the script held in [pyproject.toml](./pyproject.toml#L3).
    If errors are occurring `poetry install` (installs the virtual environment and all given requirements)

- `poetry shell` (activates and enters the virtual environment)

- `poetry run python -m unittest discover` (runs all tests). Alternatively `poetry run python -m pytest tests` to use pytest for test execution.
