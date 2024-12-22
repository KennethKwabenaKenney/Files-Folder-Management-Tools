# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:56:27 2024

@author: kenneyke
"""

import os
import pandas as pd

def create_dataset_pair(directory):
    # Get the parent directory of the specified directory
    parent_directory = os.path.dirname(directory)

    # Get the last folder name from the specified directory
    last_folder = os.path.basename(os.path.normpath(directory))

    # Get a list of all CSV files in the directory and sort them numerically
    csv_files = sorted([file for file in os.listdir(directory) if file.endswith('.csv') and file.split('_')[0].isdigit()], key=lambda x: int(x.split('_')[0]))

    # Create an empty list to store the pairs
    pairs = []

    # Pair each file with every other file in reverse order
    for i, file1 in enumerate(csv_files):
        for j, file2 in enumerate(csv_files):
            pairs.append({'Training': os.path.join(directory, file1), 'Testing': os.path.join(directory, file2)})

    # Create a DataFrame from the list of pairs
    pairs_df = pd.DataFrame(pairs)

    # Construct the output file path in the parent directory with the last folder name and "DatasetPair" appended
    output_filename = f"{last_folder}_DatasetPair.csv"
    output_file = os.path.join(parent_directory, output_filename)

    # Save the pairs DataFrame to the output CSV file
    pairs_df.to_csv(output_file, index=False)

# Specify the directory containing the CSV files
directory_path = r'D:\ODOT_SPR866\My Label Data Work\New Manual Labelling\6_Analysis\2HWY_Site-Site'

# Call the function to create the dataset pair and save it to the parent directory with the automatically generated filename
create_dataset_pair(directory_path)
print("Done!")
