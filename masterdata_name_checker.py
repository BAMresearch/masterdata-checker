# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:20:50 2023

@author: cmadaria
"""

import re


def name_checker(file_path):
    file_name = file_path.split("/")[-1]
    
    # Define the pattern for a valid file name
    pattern = r"^(collection_type|object_type|dataset_type|vocabulary)_([\w.]+)_(v\d+)_([a-zA-Z0-9]+(?:\.[0-9]+)?)_([a-zA-Z0-9]+)\.(xls|xlsx)$"
 
    # Check if the file name matches the pattern
    match = re.match(pattern, file_name)

    if match:
        # Extract parts of the file name
        entity_type, entity_name, version, division, contact_person, extension = match.groups()
        print(entity_type, entity_name, version, division, contact_person, extension)
        return ["File name: OK!", True]
    else:
        # Return specific errors and positions
        errors = []
        file_name = file_name.split(".xls")
        
        if len(file_name) < 2:
            raise UserFailureException("Error: Invalid file type. The file should be an Excel file (.xls or .xlsx)")
        
        else:
            file_parts = file_name[0].split("_")
            if len(file_parts) < 5:
                errors.append("Invalid name format. The name should contain different fields separated by underscores (_). Consult the wiki to see which ones.")
                return ["\n".join(errors), False]
            creator = file_parts.pop(-1)
            section = file_parts.pop(-1)
            version = file_parts.pop(-1)
            etype = file_parts.pop(0)
            if (etype == "object" or etype == "collection" or etype == "dataset"):
                etype = etype + "_" + file_parts.pop(0)
            code = "_".join(file_parts)
            
            if not re.match(r"^(collection_type|object_type|dataset_type|vocabulary)$", etype):
                errors.append("Invalid entity type at position 1.")
            if not re.match(r"^([\w.]+)$", code):
                errors.append("Invalid entity name at position 2.")
            if not re.match(r"^(v\d+)$", version):
                errors.append("Invalid version at position 3.")
            if not re.match(r"^([a-zA-Z0-9]+(?:\.[0-9]+)?)$", section):
                errors.append("Invalid division at position 4.")
            if not re.match(r"^[a-zA-Z0-9]+$", creator):
                errors.append("Invalid contact person at position 5.")
            
            return ["\n".join(errors), False]
        
class UserFailureException(Exception):
    pass