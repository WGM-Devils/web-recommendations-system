import os
import sys

def baseuri():
    return 'https://klingt-gut.onrender.com/api'

# download all needed libarys using pip
def setup_libarys():
    sys.stdout.write("Downloading libarys...")
    os.system('pip install requests')
    os.system('pip install pandas')
    os.system('pip install python-dateutil')
    os.system('pip install numpy')
    sys.stdout.write("Done\n")

# check if all needed libarys are installed
def check_libarys():
    try:
        import requests
        import pandas as pd
        import dateutil
        import numpy
    except ImportError:
        print("Please install all needed libarys")
        setup_libarys()

# check if all needed files are present
def check_files():
    # files to check:
    # hashtags_for_user/base_info.py
    # hashtags_for_user/hashtags_from_post.py
    # hashtags_for_user/post_score.py
    
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

# main function
def main():
    check_libarys()
    check_files()
    print("Setup complete")

if __name__ == "__main__":
    main()