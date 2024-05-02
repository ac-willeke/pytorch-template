# Project Structure

The following files are included in this template:

1. Installation config files:
    - [pyproject.toml](../pyproject.toml) to set your project dependencies.
    - [pre-commit-config.yaml](../pre-commit-config.yaml) to set your pre-commit hooks.
    - [Makefile](../Makefile) to set project commands for installation, testing, and publishing.

2. Project config files:
    - [config/.env](../config/template.env) to set your environment variables
    - [config/catalog.yaml](../config/config.yaml) to store your data paths and project metadata. 
    - [config/parameters.yaml](../config/params.yaml) to set your model parameters.
    - [config/logging.yaml](../config/logging.yaml) to set your logging configuration

3. Python config files:
    - [config.py](../src/config.py) to load your project configuration.
    - [logger.py](../src/logger.py) to set up your logging configuration.
    - [utils.py](../src/utils.py) project utility methods.
    - [decorators.py](../src/decorators.py) project decorators.

6. A sample project to test the *src package* in this template ([here](../pilot_project/main.py)).

5. A test-suite using the pytest framework to test the *src package* in this template ([here](tests/test_utils.py)).

6. Documentation:
    
    Guides with documentation on: 
    - how to set up a python project in linux
    - how to use classes and methods in python
    - cheatsheet for linux shell commands

## Tree structure

```bash
# project structure
\pytorch-template
    ├── .devcontainer
    │   └── template_devcontainer.json
    ├── config
    │   ├── .env
    │   ├── catalog.yaml
    │   ├── logging.yaml
    │   └── parameters.yaml
    ├── docs
    │   ├── changelog.md        
    │   ├── todo.md             
    │   └── project_structure.md  
    ├── log
    │   └── .gitkeep            
    ├── notebooks
    │   ├── 01_notebook.ipynb 
    │   └── 02_notebook.ipynb
    ├── pilot_project
    │   ├── main.py
    │   └── settings.py
    ├── src
    │   ├── sub-package
    │   │   ├── __init__.py
    │   ├── __init__.py
    │   ├── config.py
    │   ├── decorators.py
    │   ├── logger.py
    │   └── utils.py
    ├── tests
    │   ├── __init__.py
    │   ├── test_config.py
    │   ├── test_config.yaml
    │   ├── test_logger.py
    │   └── test_utils.py
    ├── .gitignore
    ├── .pre-commit-config.yaml
    ├── Dockerfile
    ├── LICENSE
    ├── Makefile
    ├── poetry.lock
    ├── pyproject.toml
    └── README.md
```