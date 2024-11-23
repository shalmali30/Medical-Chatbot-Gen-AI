import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

list_of_files = [
"src/__init__.py",  #constructor file
"src/helper.py",
"src/prompt.py"  #all functions will be here
".env",
"requirements.txt",
"setup.py",
"app.py",
"research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)    #Path function is used to handle all types of path in different OS / or \. it will auto take the path for win or macos
    filedir, filename = os.path.split(filepath) 


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  #checking if filesize is 0. if not will not delete and create
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
