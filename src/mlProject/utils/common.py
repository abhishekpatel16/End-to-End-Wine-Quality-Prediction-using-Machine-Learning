import os  # Importing the os module to interact with the operating system
from box.exceptions import BoxValueError  # Importing specific exception from box module
import yaml  # Importing yaml module to read and write YAML files
from mlProject import logger  # Importing logger from mlProject for logging
import json  # Importing json module to handle JSON files
import joblib  # Importing joblib for saving and loading binary files
from ensure import ensure_annotations  # Importing ensure_annotations to enforce function annotations
from box import ConfigBox  # Importing ConfigBox to handle dictionary-like objects
from pathlib import Path  # Importing Path from pathlib for file path manipulations
from typing import Any  # Importing Any for type hinting any data type


@ensure_annotations  # Enforcing type annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other exception occurs.

    Returns:
        ConfigBox: A dictionary-like object containing YAML file data.
    """
    try:
        with open(path_to_yaml) as yaml_file:  # Opening the YAML file in read mode
            content = yaml.safe_load(yaml_file)  # Loading YAML content safely
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")  # Logging success message
            return ConfigBox(content)  # Returning content as ConfigBox
    except BoxValueError:  # Handling empty YAML file error
        raise ValueError("YAML file is empty")
    except Exception as e:  # Handling any other exceptions
        raise e  
    

@ensure_annotations  # Enforcing type annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories if they do not exist.
    
    Args:
        path_to_directories (list): List of directory paths to be created.
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Creating directory if it does not exist
        if verbose:
            logger.info(f"Created directory at: {path}")  # Logging success message


@ensure_annotations  # Enforcing type annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary as a JSON file.
    
    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to be saved in JSON format.
    """
    with open(path, "w") as f:  # Opening file in write mode
        json.dump(data, f, indent=4)  # Writing data to JSON file with indentation
    
    logger.info(f"JSON file saved at: {path}")  # Logging success message


@ensure_annotations  # Enforcing type annotations
def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file.
    
    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as a ConfigBox (acts like a dictionary with attribute access).
    """
    with open(path) as f:  # Opening file in read mode
        content = json.load(f)  # Loading JSON content

    logger.info(f"JSON file loaded successfully from: {path}")  # Logging success message
    return ConfigBox(content)  # Returning data as ConfigBox


@ensure_annotations  # Enforcing type annotations
def save_bin(data: Any, path: Path):
    """Saves data as a binary file using joblib.
    
    Args:
        data (Any): Data to be saved in binary format.
        path (Path): Path to save the binary file.
    """
    joblib.dump(value=data, filename=path)  # Saving data using joblib
    logger.info(f"Binary file saved at: {path}")  # Logging success message


@ensure_annotations  # Enforcing type annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file.
    
    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Object stored in the file.
    """
    data = joblib.load(path)  # Loading binary data using joblib
    logger.info(f"Binary file loaded from: {path}")  # Logging success message
    return data  # Returning loaded data


@ensure_annotations  # Enforcing type annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in kilobytes (KB).
    
    Args:
        path (Path): Path of the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Getting file size in KB and rounding it
    return f"~ {size_in_kb} KB"  # Returning formatted file size string
