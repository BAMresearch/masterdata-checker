"""
Created on Tue Nov 28 16:01:50 2023

@author: cmadaria
"""

import getpass
import sys
import tkinter as tk
from tkinter import filedialog

from pybis import Openbis

from masterdata_checker.content import content_checker
from masterdata_checker.csv_visualizer import generate_csv_and_download
from masterdata_checker.entity import entity_checker
from masterdata_checker.name import name_checker

# Access command-line arguments
if len(sys.argv) < 3:
    print('Usage: python master_checker.py <username> <instance>')
    sys.exit(1)

username = sys.argv[1]
instance = sys.argv[2]

# Prompt for the password
password = getpass.getpass(prompt='Please enter your password: ')

# Now you have access to `username`, `instancename`, and `password`
print(f'Username: {username}, Instance: {instance}')

url = f'https://{instance}.datastore.bam.de/'
o = Openbis(url)
o.login(username, password, save_token=True)


def open_file_dialog():
    file_path = filedialog.askopenfilename(title='Select a File')
    print(file_path)
    if file_path:
        selected_file_label.config(text=f'{file_path}')
        check_button.pack(
            side=tk.TOP, pady=5
        )  # Show the check_button under the open_button
        result_label.pack_forget()  # Hide the result label
        content_button.pack_forget()  # Hide the Check Instance Content button
        resize_window()


def resize_window():
    app.update_idletasks()  # Ensure all widgets are updated
    original_height = 150
    new_width = (
        max(selected_file_label.winfo_reqwidth(), result_label.winfo_reqwidth()) + 20
    )
    new_height = (
        original_height
        + selected_file_label.winfo_reqheight()
        + result_label.winfo_reqheight()
        + 20
    )  # 20 is the total padding
    app.geometry(f'{new_width}x{new_height}')


def check_file():
    # Get the file name from the selected_file_label
    file_path = selected_file_label.cget('text')
    file_name = file_path.split('/')[-1]

    result_name = str(name_checker(file_name)[0])
    name_ok = name_checker(file_name)[1]
    result_content = str(content_checker(file_path, name_ok))
    result_entity = str(entity_checker(file_path, o))
    result_format = (
        'CHECKED NAME:'
        + '\n-------------\n'
        + result_name
        + '\n'
        + '\nCHECKED CONTENT:'
        + '\n-------------\n'
        + result_content
        + '\n'
        + '\nCHECKED ENTITY'
        + '\n-------------\n'
        + result_entity
    )

    # Display the result under the "Check File" button
    result_label.config(state=tk.NORMAL, height=15)
    result_label.delete(1.0, tk.END)
    result_label.insert(tk.END, result_format)
    result_label.pack(pady=10)

    # Adjust the window size based on the result text
    resize_window()


def show_content():
    # Get the file name from the selected_file_label
    content = generate_csv_and_download(o, instance)
    # Display the result under the "Check File" button
    check_button.pack_forget()
    result_label.config(state=tk.NORMAL, height=3)
    result_label.delete(1.0, tk.END)
    result_label.insert(tk.END, content)
    result_label.tag_add('center', '1.0', 'end')
    result_label.tag_configure('center', justify='center')
    result_label.pack(pady=10)

    # Adjust the window size based on the result text
    resize_window()


# Create the main application window
app = tk.Tk()
app.title('openBIS Masterdata Format Checker')  # Set the title
app.geometry('400x250')  # Set the window size (width x height)

# Create a label for the title
title_label = tk.Label(app, text='openBis Masterdata Checker', font=('Helvetica', 16))
title_label.pack(pady=10)

# Create a label for the selected file
selected_file_label = tk.Label(app, text='')
selected_file_label.pack()

# Create a button to trigger the file dialog
open_button = tk.Button(app, text='Select File...', command=open_file_dialog)
open_button.pack(pady=20)

# Create a button to visualize instance content
content_button = tk.Button(app, text='Check Instance Content', command=show_content)
content_button.pack(pady=20)

# Create a "CHECK" button (initially hidden)
check_button = tk.Button(app, text='Check File!', command=check_file)
check_button.pack_forget()

# Create a label to display the result
result_label = tk.Text(app, wrap=tk.WORD, height=15, state=tk.DISABLED)
result_label.pack_forget()  # Initially hide the result label

# Start the main event loop
app.mainloop()
