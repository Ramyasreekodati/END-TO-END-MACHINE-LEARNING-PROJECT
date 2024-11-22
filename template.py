import os  #   which helps interact with the operating system (like working with files or directories)
from pathlib import Path  # Imports 'Path' from the 'pathlib' module to handle file paths easily
import logging  #  to create logs for debugging or tracking code execution

logging.basicConfig(level=logging.INFO,format="[%(asctime)s]:%(message)s:" )
#logging.INFO says that  logs with this level or higher (like WARNING, ERROR, etc.) will be shown.
#Logs below this level (like DEBUG) will be ignored.
#%(asctime)s: shows the  timestamp (date and time) when the log message was created.
#%(message)s:  shows the actual log message that you want to display.

project_name="wine quality"

list_of_files = [
    f"src/{project_name}/__init__.py",  # Main project initialization file
    f"src/{project_name}/components/__init__.py",  # Components folder initialization file
    f"src/{project_name}/utils/__init__.py",  # Utilities folder initialization file
    f"src/{project_name}/utils/common.py",  # Common utility functions
    f"src/{project_name}/config/__init__.py",  # Config folder initialization file
    f"src/{project_name}/config/configuration.py",  # Configuration file
    f"src/{project_name}/pipeline/__init__.py",  # Pipeline folder initialization file
    f"src/{project_name}/entity/__init__.py",  # Entity folder initialization file
    f"src/{project_name}/entity/config_entity.py",  # Config entity definition file
    f"src/{project_name}/constants/__init__.py",  # Constants folder initialization file
    "config/config.yaml",  # Configuration YAML file
    "params.yaml",  # Parameters YAML file
    "schema.yaml",  # Schema definition YAML file
    "main.py",  # Main entry point of the project
    "app.py",  # Application setup file
    "requirements.txt",  # List of project dependencies
    "setup.py",  # Project setup file
    "research/trials.ipynb",  # Jupyter notebook for research trials
    "templates/index.html",  # Main HTML template
    "test.py"  # Test file for the project
]

#Windows uses backslashes, while other operating systems use forward slashes. To prevent this kind of problem, we use Path.

from pathlib import Path
import os
import logging

for filepath in list_of_files:
    filepath = Path(filepath)  # Converts the string filepath into a Path object
    filedir, filename = os.path.split(filepath)  # Splits the filepath into directory and filename

    # *******If the directory doesn't exist, create it********
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Creates the directory if it doesn't exist, doesn't raise an error if it already exists
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # *******If the file doesn't exist or is empty, create it*********
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # if the file is not exists or file size is 0 create the file other than don't creat it 
        with open(filepath, "w") as f:
            pass  # Just creates an empty file
        logging.info(f"Creating empty file: {filepath}")

    # If the file already exists and isn't empty
    else:
        logging.info(f"{filename} already exists")


"""
what is directory path ?
A directory path refers to the location or folder where files are stored on your computer or in a system. 
It shows the hierarchy of folders leading to a specific location.

    Windows: C:\Users\radhakrishna\Documents\Projects

what is file path ?
A file path refers to the complete location of a specific file,
which includes the directory path as well as the file name and its extension (e.g., .txt, .py, .jpg).
    Windows: C:\Users\randhakrihna\Documents\Projects\file.txt
"""