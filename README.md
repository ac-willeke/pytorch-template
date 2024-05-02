pytorch-template
==============================

**repo-status: work in progress**

This is a template for a pytorch project on linux. 

The documentation folder `docs` provides basic documenation on how to set up a python project in a linux environment. The [Project structure](docs/project_structure.md) shows the organization and overview of all files included in this template. 

## Getting Started 

Read the [Python Set Up Guide](docs/python_set_up.md) for a detailed description of the tools and how to set up Python projects in Linux. Below are the steps to set up and configure this specific template:

1. Click on the green button "Use this template" on GitHub.
2. Open VS Code and clone the repository.
3. Install global tools for linting etc. 
    - `make help` to see the available commands.
    - `make install-global` to install packages such as pre-commit, poetry, and black globally using pipx.
4. Set up linting and pre-commit hooks:
    - `make codestyle` to run black, isort and ruff.
    - `make pre-commit` to run pre-commit on all files.

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

### Configure your paths and parameters

Set up and check the project configuration files:
- set your environment variables in the [template.env](config/template.env). 
Rename to .env, *do not commit to git!!*
- set your data paths: [catalog.yaml](config/config.yaml) 
- set your model parameters: [parameters.yaml](config/params.yaml)
- check your logging configuration: [logging.yaml](config/logging.yaml)

Test that your configuration files are set up correctly by running the following command:

```bash
# Run the test script
python src/py-scripts/test_config.py
```

### Scripts and Notebooks

For each project you can create a notebook in the `notebooks/` directory. The notebooks are designed to be run in a Jupyter or Colab environment and they utilize the scripts in the `src/` directory. 

**Note**: If you run the notebooks in Colab, you will need to upload the `/data` and `/src` directories to the Colab environment.

```python
# upload the src/ directory to the Colab environment
from google.colab import files
uploaded = files.upload()

# unzip the file
!unzip src.zip
!ls src
```


### TODO

7. Run the tests:
    - `make poetry-test` to run all tests.
    - Run from VS Code: testing > configure python tests > pytest
8. Run pre-commit hooks and commit your changes:
    - `git add .` to add all files to the staging area.
    - `make pre-commit` to run pre-commit on all files.
    - `git commit -m "commit message"` to commit your changes.


### PyTorch Workflow






### References
-
-




