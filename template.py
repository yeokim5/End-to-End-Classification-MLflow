import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",  # Placeholder to track the GitHub Actions workflows folder in version control
    f"src/{project_name}/__init__.py",  # Initializes the cnnClassifier package
    f"src/{project_name}/components/__init__.py",  # Initializes the components module for model-building components
    f"src/{project_name}/utils/__init__.py",  # Initializes the utils module for utility functions
    f"src/{project_name}/config/__init__.py",  # Initializes the config module for configuration handling
    f"src/{project_name}/config/configuration.py",  # Contains logic to parse and manage config settings
    f"src/{project_name}/pipeline/__init__.py",  # Initializes the pipeline module for training and prediction workflows
    f"src/{project_name}/entity/__init__.py",  # Initializes the entity module for structured data schemas or config entities
    f"src/{project_name}/constants/__init__.py",  # Initializes the constants module to store project-wide constants
    "config/config.yaml",  # YAML file with project configurations such as paths and environment settings
    "dvc.yaml",  # Defines DVC stages and pipelines for data/model version control
    "params.yaml",  # Stores hyperparameters and other training configuration values
    "requirements.txt",  # Lists all Python dependencies required to run the project
    "setup.py",  # Used to package the project and define its metadata and dependencies
    "research/trials.ipynb",  # Notebook for prototyping, experimentation, or model trials
    "templates/index.html"  # HTML template for a basic web interface (e.g., for model inference)
]




for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")