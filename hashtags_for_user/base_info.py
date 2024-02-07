import os
import sys

def baseuri():
    """
    Returns the base URI for the API.

    Returns:
        str: The base URI for the API.
    """
    return 'https://klingt-gut.onrender.com/api'

def setup_libarys():
    """
    Downloads and installs the required libraries using pip.
    """
    sys.stdout.write("Downloading libraries...")
    os.system('pip install requests')
    os.system('pip install pandas')
    os.system('pip install python-dateutil')
    os.system('pip install numpy')
    sys.stdout.write("Done\n")

def check_libarys():
    """
    Checks if all the required libraries are installed.
    If any library is missing, it installs them using the `setup_libarys` function.
    """
    try:
        import requests
        import pandas as pd
        import dateutil
        import numpy
    except ImportError:
        print("Please install all required libraries")
        setup_libarys()

def check_files():
    """
    Check if the required files exist in the specified directory.

    This function checks for the existence of the following files:
    - base_info.py
    - hashtags_from_post.py
    - post_score.py

    If any of these files are missing, the function prints an error message and exits the program.
    """
    if os.path.isfile("./hashtags_for_user/base_info.py"):
        pass
    else:
        print("File 'base_info.py' is missing")
        exit()
    if os.path.isfile("./hashtags_for_user/hashtags_from_post.py"):
        pass
    else:
        print("File 'hashtags_from_post.py' is missing")
        exit()
    if os.path.isfile("./hashtags_for_user/post_score.py"):
        pass
    else:
        print("File 'post_score.py' is missing")
        exit()

def main():
    """
    The entry point of the program.
    It checks the libraries, files, and prints a setup complete message.
    """
    check_libarys()
    check_files()
    print("Setup complete")

if __name__ == "__main__":
    main()