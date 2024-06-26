pytorch-template
==============================

**repo-status: work in progress**

This is a template for a pytorch project on linux.

The documentation folder `docs` provides basic documenation on how to set up a python project in a linux environment. The [Project structure](docs/project_structure.md) shows the organization and overview of all files included in this template.

## Getting Started

Read the [Python Set Up Guide](docs/guides/python_setup_guide.md) for a detailed description of the tools and how to set up Python projects in Linux. Below are the steps to set up and configure this specific template:

1. Click on the green button "Use this template" on GitHub.
2. Open VS Code and clone the repository.
3. Install global tools for linting etc.
    - `make help` to see the available commands.
    - `make install-global` to install packages such as pre-commit, poetry, and black globally using pipx.

### Set up a Virtual Environment

You can use the `pyproject.toml` file  to set up a virtual environment. This ensures all Python dependencies and the scripts in `src\py-scripts` are installed in the environment.

Here we use Poetry as the package manager. The [Python Set Up Guide](docs/python_set_up.md) provide more information on poetry and other package managers such as pipenv and conda.

To set up a Poetry virtual environment, follow these steps:

```bash
# Navigate to your project directory where your pyproject.toml is located
cd /path/to/your/project

# Install the project dependencies
poetry install

# Activate the virtual environment
poetry shell
```

In Visual Studio Code, you can set the Python Interperater to the poetry virtual environment by clicking on the Python version in the footer.
- Select Interpreter *project-name-xxxxx-py.x.xx (poetry)*
- Path tot the virtual environment: `/home/user.name/.cache/pypoetry/virtualenvs/pytorch-template-wSTEexrb-py3.10/bin/python`

### Configure your paths and parameters

Set up and check the project configuration files:
- set your environment variables in the [template.env](config/template.env).
Rename to .env, *do not commit to git!!*
- set your data paths: [catalog.yaml](config/config.yaml)
- set your model parameters: [parameters.yaml](config/params.yaml)
- check your logging configuration: [logging.yaml](config/logging.yaml)

Test that your configuration files are set up correctly by running the following command:

```bash
# Test your conifguration
python src/config.py

# should print out the path to your project data directory
> Loading catalog...
> Project data directory: /path/to/your/project/data
```

### Scripts and Notebooks

For each project you can create a notebook in the `notebooks/` directory. The notebooks are designed to be run in a Jupyter or Colab environment and they utilize the scripts in the `src/` directory.

**Note**: If you run the notebooks in Colab, you will need to upload the `/data`, `/src` and `/config` directories to the Colab environment. You can do this by zipping the directories and uploading them to Colab.

```python
# upload the src/ directory to the Colab environment
from google.colab import files
uploaded = files.upload()

# unzip the file
!unzip src.zip
!ls src
```

See [notebook-template](notebooks/notebook-template.ipynb) for an example of how to configure your notebook for use in Colab. This includes uploading of files, adding your local modules to the path, setting up logging and configuring the catalog.


## Linting and Pre-commit Hooks

It is recommended to run pre-commit hooks and linting before committing your code. This ensures that the code is formatted correctly.

Use the following commands to run linting and pre-commit hooks:
- `make codestyle` to run black, isort and ruff.
- `make pre-commit` to run pre-commit on all files.

Linters creates cache directories starting with `.` in the project root. Add these to your `.gitignore` file. You can also clean the whole project by running `make clean`.

## List of usefull VS Code extensions

**Python**
- Python
- Pylance
- Python Debugger
- Python Environment Manager
- Python Extension Pack

**Jupyter**
- Jupyter
- Jupyter Cell Tags

**Maps, Figures and Documentation**
- Geo Data Viewer  (view vectors)
- Draw.io
- Quarto
- Live Server

**Version Control**
- Git History
- Git Graph
- GitHub Copilot
- GitLab Workflow

**Containers and Remote Machines**
- Remote - SSH
- Docker
- Dev Containers
