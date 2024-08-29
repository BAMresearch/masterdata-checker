# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:35:52 2024

@author: cmadaria
"""

from pybis import Openbis
import csv
import os
from datetime import datetime

def generate_csv_and_download(username, password, instance):

    url = f"https://{instance}.datastore.bam.de/"
    o = Openbis(url)
    o.login(username, password, save_token=True)
 
    header = ["INSTANCE", "DATE"]
    
    current_date = datetime.now().strftime("%d-%m-%Y")
    
    info = [instance, current_date]
    
    # Fetch data from the server
    spaces = [space for space in o.get_spaces()]
    projects = [project.code for project in o.get_projects()]
    experiment_types = [exp for exp in o.get_experiment_types()]
    object_types = [obj for obj in o.get_object_types() if obj.code != "UNKNOWN"]
    material_types = [material for material in o.get_material_types()]
    dataset_types = [dataset for dataset in o.get_dataset_types()]
    vocabs = [vocab.code for vocab in o.get_vocabularies()]
    plugins = [plug.name for plug in o.get_plugins()]
    
    masterdata_headers = [f"SPACES ({len(spaces)})", f"PROJECTS ({len(projects)})", f"EXPERIMENT TYPES ({len(experiment_types)})", 
                          f"OBJECT TYPES ({len(object_types)})", f"DATASET TYPES ({len(dataset_types)})",
                          f"VOCABULARIES ({len(vocabs)})", f"PLUGINS ({len(plugins)})", f"MATERIAL TYPES ({len(material_types)})"]
    
    
    # Combine master data into a list of lists
    masterdata = [
        spaces,
        projects,
        experiment_types,
        object_types,
        dataset_types,
        vocabs,
        plugins,
        material_types
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
        
        props_by_obj = []
        
        for obj in object_types:
            if obj.code == "UNKNOWN":
                continue
            props = []
            for prop in obj.get_property_assignments():
                props.append(f"{prop.code} ({str(prop.dataType).lower()})")
            props_by_obj.append(props)
            
        # Determine the maximum length of the object properties
        max_length_props = max(len(properties) for properties in props_by_obj)
        
        # Write the master data vertically
        for i in range(max_length_props):
            row = []
            for prop_list in props_by_obj:
                if i < len(prop_list):
                    row.append(prop_list[i])
                else:
                    row.append("")  # Append empty string if the list is shorter
            writer.writerow(row)
        
    return f"CSV file '{filename}' has been created."
