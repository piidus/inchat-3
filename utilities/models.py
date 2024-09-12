import os
import sqlite3
from sqlite3 import Error
import platform

# from .log_help import log

#create folder if not exist in 
def create_folder(folder_name = 'INCHAT'):
    try:
        if platform.system == 'Android':
            path = f"/storage/emulated/0/{folder_name}"
        else:
            path = f"{folder_name}"
        
        # Create the folder
        os.makedirs(path, exist_ok=True)
        
        return True
    except OSError as e:
        
        return False
    

