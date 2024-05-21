# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:35:52 2024

@author: cmadaria
"""

from pybis_connection import connect
import csv
import os
from datetime import datetime

o = connect('serverA')

url = o.url

header = ["INSTANCE", "DATE"]

instance = url.split("//")[1].split(".")[0]

current_date = datetime.now().strftime("%d-%m-%Y")

info = [instance, current_date]


masterdata_headers = ["SPACES", "PROJECTS", "EXPERIMENT TYPES", "OBJECT TYPES", "MATERIAL TYPES", "DATASET TYPES", "VOCABULARIES", "PLUGINS"]

# Fetch data from the server
spaces = [space for space in o.get_spaces()]
projects = [project.code for project in o.get_projects()]
experiment_types = [exp for exp in o.get_experiment_types()]
object_types = [obj for obj in o.get_object_types()]
material_types = [material for material in o.get_material_types()]
dataset_types = [dataset for dataset in o.get_dataset_types()]
vocabs = [vocab.code for vocab in o.get_vocabularies()]
plugins = [plug.name for plug in o.get_plugins()]

# Combine master data into a list of lists
masterdata = [
    spaces,
    projects,
    experiment_types,
    object_types,
    material_types,
    dataset_types,
    vocabs,
    plugins
]
# Directory name based on instance
directory = f"{instance}_data"

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# File path
filename = os.path.join(directory, f"{instance}_{datetime.now().strftime('%d%m%Y')}.csv")

# Write data to CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the instance and date headers
    writer.writerow(["INSTANCE", "DATE"])
    
    # Write the instance and date info
    writer.writerow(info)
    
    # Write empty row
    writer.writerow("")
    
    # Write the master data headers
    writer.writerow(masterdata_headers)
    
    # Determine the maximum length of the master data lists
    max_length = max(len(data) for data in masterdata)
    
    # Write the master data vertically
    for i in range(max_length):
        row = []
        for data in masterdata:
            if i < len(data):
                row.append(data[i])
            else:
                row.append("")  # Append empty string if the list is shorter
        writer.writerow(row)
        
    # Write empty row
    writer.writerow("")
    
    writer.writerow(["PROPERTY LIST BY OBJECT TYPE"])
        
    # Write another header row with the content of object_types horizontally
    writer.writerow(object_types)
    
print(f"CSV file '{filename}' has been created.")
