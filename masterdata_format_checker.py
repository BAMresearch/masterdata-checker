# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 16:01:50 2023

@author: cmadaria
"""

import tkinter as tk
from tkinter import filedialog
import re
import openpyxl

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a File")
    print(file_path)
    if file_path:
        selected_file_label.config(text=f"{file_path}")
        check_button.pack(side=tk.TOP, pady=5)  # Show the check_button under the open_button
        result_label.pack_forget()  # Hide the result label
        resize_window()

def resize_window():
    app.update_idletasks()  # Ensure all widgets are updated
    original_height = 150
    new_width = max(selected_file_label.winfo_reqwidth(), result_label.winfo_reqwidth()) + 20
    new_height = original_height + selected_file_label.winfo_reqheight() + result_label.winfo_reqheight() + 20  # 20 is the total padding
    app.geometry(f"{new_width}x{new_height}")

def check_file():
    # Get the file name from the selected_file_label
    file_path = selected_file_label.cget("text")
    file_name = file_path.split("/")[-1]
    
    result_name = name_checker(file_name)
    result_content = content_checker(file_path)

    # Display the result under the "Check File" button
    result_label.config(text=result_name)
    result_label.pack(pady=10)

    # Adjust the window size based on the result text
    resize_window()

def name_checker(file_name):
    # Define the pattern for a valid file name
    pattern = r"^(collection_type|object_type|dataset_type|vocabulary)_([\w.]+)_(v\d+)_([a-zA-Z0-9]+(?:\.[0-9]+)?)_([a-zA-Z0-9]+)\.(xls|xlsx)$"
 
    # Check if the file name matches the pattern
    match = re.match(pattern, file_name)

    if match:
        # Extract parts of the file name
        entity_type, entity_name, version, division, contact_person, extension = match.groups()
        print(entity_type, entity_name, version, division, contact_person, extension)
        return "File name: OK!"
    else:
        # Return specific errors and positions
        errors = []
        file_name = file_name.split(".xls")
        
        if len(file_name) < 2:
            errors.append("Invalid file format. Only .xls and .xlsx accepted")
            return errors
        
        else:
            file_parts = file_name[0].split("_")
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
            
            return "\n".join(errors)
        
def content_checker(file_path):
    workbook = openpyxl.load_workbook(file_path)

    # Select the specific sheet (replace 'Sheet1' with your sheet name)
    sheet = workbook['Sheet1']

    # Access a specific cell (e.g., cell A1)
    cell_value_A1 = sheet['A1'].value
    print(f"Value in cell A1: {cell_value_A1}")

    # Access a range of cells (e.g., from A1 to B2)
    cell_range_values = []
    for row in sheet.iter_rows(min_row=1, max_row=2, min_col=1, max_col=2):
        for cell in row:
            cell_range_values.append(cell.value)

    print(f"Values in range A1:B2: {cell_range_values}")

    # Close the workbook after use
    workbook.close()

# Create the main application window
app = tk.Tk()
app.title("openBIS Masterdata Format Checker")  # Set the title
app.geometry("400x150")  # Set the window size (width x height)

# Create a label for the title
title_label = tk.Label(app, text="openBis Masterdata Format Checker", font=("Helvetica", 16))
title_label.pack(pady=10)

# Create a label for the selected file
selected_file_label = tk.Label(app, text="")
selected_file_label.pack()

# Create a button to trigger the file dialog
open_button = tk.Button(app, text="Select File...", command=open_file_dialog)
open_button.pack(pady=20)

# Create a "CHECK" button (initially hidden)
check_button = tk.Button(app, text="Check File!", command=check_file)
check_button.pack_forget()

# Create a label to display the result
result_label = tk.Label(app, text="")
result_label.pack_forget()  # Initially hide the result label

# Start the main event loop
app.mainloop()


