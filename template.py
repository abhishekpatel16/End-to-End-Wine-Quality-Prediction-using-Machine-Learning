import os  # Importing the os module to interact with the operating system
from pathlib import Path  # Importing Path from pathlib to handle file paths efficiently
import logging  # Importing logging module for logging information

# Configuring logging to display messages with timestamps
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Defining the project name
project_name = "mlProject"

# List of files and directories to be created
list_of_files = [
    f"src/{project_name}/__init__.py",  # Package initializer for src/mlProject
    f"src/{project_name}/components/__init__.py",  # Package initializer for components module
    f"src/{project_name}/utils/__init__.py",  # Package initializer for utils module
    f"src/{project_name}/utils/common.py",  # Common utility functions
    f"src/{project_name}/config/__init__.py",  # Package initializer for config module
    f"src/{project_name}/config/configuration.py",  # Configuration script
    f"src/{project_name}/pipeline/__init__.py",  # Package initializer for pipeline module
    f"src/{project_name}/entity/__init__.py",  # Package initializer for entity module
    f"src/{project_name}/entity/config_entity.py",  # Configuration entity script
    f"src/{project_name}/constants/__init__.py",  # Package initializer for constants module
    "config/config.yaml",  # YAML configuration file
    "params.yaml",  # Parameters file
    "schema.yaml",  # Schema definition file
    "main.py",  # Main script for execution
    "app.py",  # Application script
    "requirements.txt",  # Dependencies list
    "setup.py",  # Setup script for installation
    "research/trials.ipynb",  # Jupyter notebook for research
    "templates/index.html"  # HTML template file
]

# Loop through each file path in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string path to Path object
    filedir, filename = os.path.split(filepath)  # Extract directory and filename

    # Check if directory exists; if not, create it
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directories as needed
        logging.info(f"Creating directory; {filedir} for the file: {filename}")  # Log directory creation

    # Check if file exists and is not empty; if not, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")  # Log file creation
    else:
        logging.info(f"{filename} already exists")  # Log if file already exists