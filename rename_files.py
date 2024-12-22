# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:43:23 2024

@author: kenneyke
"""

import os

def re_edit_name_of_files(folder_path):
    # List all files in the specified folder
    files = os.listdir(folder_path)

    for file_name in files:
        # Check if the file has .laz extension and contains "_updated"
        if file_name.endswith(".laz") and "_updated" in file_name:
            # Generate the new file name by removing "_updated"
            new_file_name = file_name.replace("_updated", "")

            # Construct the full paths for the old and new files
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {file_name} -> {new_file_name}")

# Get the folder path from the user through console input
folder_path = input("Enter the folder path containing .laz files: ")

if os.path.isdir(folder_path):
    # Call the function to remove "_updated" from file names
    re_edit_name_of_files(folder_path)
    print("File renaming completed.")
else:
    print("Invalid folder path. Please provide a valid path.")
