# Linux Set Up for Python Development
This document describes how to set up a Linux environment for Python proejcts. The information is based on the documentation from [Python Packages](https://py-pkgs.org/welcome),  [DataCamp](https://www.datacamp.com) course material and [Packaging for Python](https://packaging.python.org/en/latest/tutorials/packaging-projects/). See the [cheatsheet](cheatsheet_unix_shell.md) for a quick overview of the Unix shell.


## Installation

Check your shell configuration using the command `echo $0`.

### Python

 - Check if and where Python is installed.

      ```bash
      # Standard Python Distribution
      which python3
      python3 --version
      which pip
      which pipx

      # Anaconda Distribution
      which conda
      conda --version
      ```


- Standard Python distribution

   - download and install from [python.org](https://www.python.org/downloads/)

   - add Python to your PATH
   - Install `pipx`: `python3 -m pip install pipx`
   - Configure PATH: `pipx ensurepath`
   - Close and open your shell again

- Miniconda distribution
   - download and install from [conda.io](https://docs.conda.io/en/latest/miniconda.html)

      ```bash
      # create a directory
      mkdir -p ~/miniconda3
      cd miniconda3

      # download miniconda
      wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

      # rename file to miniconda.sh
      mv Miniconda3-latest-Linux-x86_64.sh miniconda.sh

      # install miniconda
      bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

      # remove installation file
      rm -rf ~/miniconda3/miniconda.sh
      ``````
   - initialize conda

      ```bash
      ~/miniconda3/bin/conda init
      ```
   - close and re-open your shell
   - ensure that conda is up to date `conda update --all`

### Environment Management

It is best practice to use virtual environments for your Python projects. This ensures that your project dependencies are isolated from your python base installation. If you install a package using `pip install` directly, it will be installed globally and can cause conflicts with other projects. You can use different tools to create virtual environments:

- venv (Standard Python distribution)

   - `venv` is the standard tool for creating virtual environments in Python. The files `requirements.txt` and `setup.py` are used to manage the dependencies of your project.
   - create a new virtual env using venv

      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```
   - install packages using pip inside the virtual env

      ```bash
      pip install numpy pandas
      ```
   - install local package in editable mode

      ```bash
      pip install -e .
      ```


- Conda
   - create a new environment using conda

      ```bash
      conda create --name myenv python=3.8
      conda activate myenv
      ```

   - install packages using conda

      ```bash
      conda install numpy pandas
      ```

   - install packages using pip inside the conda env

      ```bash
      pip install requests
      ```

- Poetry

   - Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry also allows you to create a virtual environment for your project, so that your project is isolated from your system.

      - documentation: [poetry-docs](https://python-poetry.org/docs/)

      - install poetry: `pipx install poetry`

   - create a new virtual env based on the `pyproject.toml` file

      ```bash
      poetry install
      poetry shell
      ```

   - install packages using poetry

      ```bash
      poetry add numpy pandas
      ```






**Configuration files:**
- `pyproject.toml`: contains project information and its dependencies. project, including its dependencies. Documentation [here](https://python-poetry.org/docs/pyproject/).
- `poetry.lock`: contains the exact versions of the dependencies that were installed in your project.

The `poetry.lock` file is automatically generated and should not be edited. It contains the exact versions of the dependencies that were installed in your project.

**Poetry set-up in VS Code:**
- install poetry extension in VS Code
- install the packages defined in the `pyproject.toml` file into a virtual env using `poetry install`.
   - see https://python-poetry.org/docs/cli/ for all poetry commands.
- activate poetry environment in terminal: `poetry shell`
- set the Python Environment (bottom-left corner) to the poetry environment

| Python Distribution | Python Path | Python Version |
| ------------------- | ----------- | -------------- |
|standard distribution| `/usr/bin/python3` | `Python +3.10.12` |
|miniconda distribution| `/home/username/miniconda3/bin/conda/` | `conda +23.5.2`
| poetry package manager | `/home/username/.cache/pypoetry/virtualenvs` | `Python x.xx.x` |

## Git and Github

- install git: [git-scm.com](https://git-scm.com/download/linux)
- login to GitHub in vscode
- configure git
   ```shell
   git config --global user.name "John Doe"
   git config --global user.email johndoe@example.com
   git config --global init.defaultBranch main

   # check your settings
   git config --list --show-origin
   ```
- create `.gitignore` and add files and directories that should not be tracked by git

## Pre-commit
** pre-commit** checks certain actions before committing changes to your repository. The list of actions that are executed are defined in `.pre-commit-config.yaml`.
   - Install `pre-commit`: `pipx install pre-commit`
   - Enter into your git repository and install the hooks: `pre-commit install` (optional, but recommended)
   - de-activate pre-commit:
      - delete or comment out the lines in .pre-commit-config.yaml
      - `pre-commit uninstall`
      - `pre-commit clean`

**How to use pre-commit:**

In case you executed `pre-commit install`, `pre-commit` hooks will be executed each time you will try to commit (`git commit`). If any of the checks fail or if any files that is going to be committed is changed (because a tool refactored or cleaned it), the commit will fail.

The suggested method to use `pre-commit` is to run it before trying to commit your changes, using `pre-commit run -a`. You can run this command multiple times, to check if the changes are ready to be committed.
After all the tests succeeded, the changes can be staged (`git add`) and committed.

**Note**: Solely install pre-commit in the standard distribution, not in the miniconda distribution or project-specific poetry environment.

## Project Structure

The project structure of this template is shown [here](project_structure.md). You can use this repository as a template for your own project or create a project structure using `cookiecutter`.

```shell
which cookiecutter
cd path/to/your/project
cookiecutter <path/to/cookiecutter/template>
```

Templates:
- [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)
- [python-package-template](https://github.com/TezRomacH/python-package-template)
- [cookiecutter] (https://github.com/py-pkgs/py-pkgs-cookiecutter.git)

In Visual Studio Code you can use the default extension `vscode-cookierunner` to define default cookiecutter templates.

## Code Formatters and Linter
In this template the following code formatters and linter are used:

- [Black](https://black.readthedocs.io/en/stable/) (code formatter)

- [Isort](https://pycqa.github.io/isort/) (sorts imports)

- [Ruff](https://github.com/astral-sh/ruff) (linter)

- [pyment](https://github.com/dadadel/pyment) (docstring formatter), docstrings in this template use the Numpy style.

Example of a docstring in Numpy style for a function:

```python
class Vehicles(object):
    '''
    The Vehicles object contains lots of vehicles

    Parameters
    ----------
    arg : str
        The arg is used for ...
    *args
        The variable arguments are used for ...
    **kwargs
        The keyword arguments are used for ...

    Attributes
    ----------
    arg : str
        This is where we store arg,
    '''
    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def cars(self, distance, destination):
        '''We can't travel distance in vehicles without fuels, so here is the fuels

        Parameters
        ----------
        distance : int
            The amount of distance traveled
        destination : bool
            Should the fuels refilled to cover the distance?

        Raises
        ------
        RuntimeError
            Out of fuel

        Returns
        -------
        cars
            A car mileage
        '''
        pass

```

Example of a docstring in reStructured text style for a function:

```python
"""Summary line.

Extended description of function.

:param arg1: Description of arg1
:type arg1: int
:param arg2: Description of arg2
:type arg2: str
:returns: Description of return value
:rtype: bool
:raises ValueError: if `param2` is equal to `param1`.
```

The configuration for these tools is set in the `pyproject.toml` file.

## Makefile

**!!Likely to be removed for this template!!**


*Make* is a tool that is used for automating tasks by defining a set of instructions in a `Makefile` which is located in your projects root directory. Install make using: `sudo apt install make`

Good practices in Makefiles:
- testing, cleaning targts should be phony.
- environment setup (like tool installation) targets do not need to be phony.
- define a single .PHONY at the top of the Makefile
- group targets by functionality

A template Makefile is provided in this repository. It contains the following targets:
- `make global-install`: installs all dependencies that are not project-specific using pipx
   - pre-commit
   - black
   - isort
   - ruff
   - pyment

- `make poetry-install`: installs all dependencies that are project-specific using poetry
- `make codestyle`: runs all code quality checks (black, isort, ruff, pyment)
- `make docstring`: generates or converts docstrings to the reStructured text style using pyment
- `make cleanup`: removes all temporary files and directories






## References

- [Python Packages](https://py-pkgs.org/welcome)
- [Python](https://docs.python.org/3/)
- [Git](https://git-scm.com/doc)
- [GitHub](https://docs.github.com/en)
- [PyPI](https://pypi.org/help/)
- [Poetry](https://python-poetry.org/docs/)
- [Make](https://www.gnu.org/software/make/manual/make.html)
- [Pre-commit](https://pre-commit.com/)
- [Black](https://black.readthedocs.io/en/stable/)
- [Isort](https://pycqa.github.io/isort/)
- [Ruff](https://github.com/astral-sh/ruff)
- [pyment](https://github.com/dadadel/pyment)
