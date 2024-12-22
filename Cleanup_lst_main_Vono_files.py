# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 02:12:28 2024

@author: kenneyke
"""

import os

def clean_folders():
    # Get the path from the user
    parent_folder_path = input("Enter the parent folder path: ")

    # Check if the path exists
    if not os.path.exists(parent_folder_path):
        print("Invalid folder path.")
        return

    # Get a list of folders in the parent folder
    folders = [folder for folder in os.listdir(parent_folder_path) if os.path.isdir(os.path.join(parent_folder_path, folder))]

    # Iterate through each folder
    for folder_name in folders:
        if "_segVono" in folder_name:
            folder_path = os.path.join(parent_folder_path, folder_name)
            files = os.listdir(folder_path)
            for file_name in files:
                if file_name.endswith(".lst") or "_FieldBlk" not in file_name:
                    os.remove(os.path.join(folder_path, file_name))
                    print(f"Deleted {file_name} in folder {folder_name}")

    print("Cleanup completed.")

clean_folders()