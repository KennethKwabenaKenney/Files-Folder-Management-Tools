# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 01:57:43 2024

@author: kenneyke
"""

import os
import shutil

def organize_laz_files():
    # Get the path from the user
    folder_path = input("Enter the folder path: ")

    # Check if the path exists
    if not os.path.exists(folder_path):
        print("Invalid folder path.")
        return

    # Get a list of .laz files in the folder
    laz_files = [file for file in os.listdir(folder_path) if file.endswith(".laz")]

    # Create folders and move .laz files
    for laz_file in laz_files:
        folder_name = laz_file.replace(".laz", "")
        folder_path_new = os.path.join(folder_path, folder_name)
        
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path_new):
            os.makedirs(folder_path_new)
        
        # Move the .laz file to the new folder
        shutil.move(os.path.join(folder_path, laz_file), os.path.join(folder_path_new, laz_file))

    print("Files organized successfully.")

organize_laz_files()
