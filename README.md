# Masterdata Checker & Visualizer

Check the correctness and alignment with the BAM Data Store Project guidelines of the new entities before registering them in openBIS, through the Import utility using Excel files containing the new Objects data. 

With a clear and easy interface, and a detailed list of every present issue in the Excel files, it allows you to correct your new objects and to avoid losing time.

It is also possible to visualize the whole content of the desired openBIS instances, as long as we have credentials to access them, to check the metadata already present on the selected instance.

There is also available a Jupyter Notebook version to execute the Masterdata Checker and Visualizer directly in the Web IDE.


## Visuals
![checker1](./images/Screenshot_2024-08-26_110931.png)
![checker2](./images/Screenshot_2024-08-26_111456.png)
![checker3](./images/Screenshot_2024-08-26_111600.png)


## Requirements
- ([Python3](https://www.python.org/downloads/))

Once that you have installed latest Python version, you can use the ``pip`` command to install the following dependencies (both in your command line (cmd) or directly in a Jupyter Notebook):
- pyBIS: ``pip install pybis``
- pandas: ``pip install pandas``
- regex: ``pip install re``

Those are the basic packages that you will need.

Now, depending on the version that you are going to use, you need to install the following packages (although probably most of them will be already installed within your Python installation, but just in case that you receive any error with some of the packages, here yu have the way of installing them):

*For the Web IDE version (Jupyer Notebook)*:
- ``pip install jupyterlab`` // ``pip install notebook`` (choose one, information about [here](https://jupyter.org/install))
- CSV: ``pip install csv``
- OS: ``pip install os``
- Python Widgets: ``pip install ipywidgets``
- Time: ``pip install time``
- Tempfile: ``pip install tempfile``

*For the local UI (User Interface)*:
- TKInter: ``pip install tkinter``
- OpenPyXL: ``pip install openpyxl``


## Installation
Once that you have fulfilled all the requirements above, no more installation is needed, you can just run the main script to start using it:

From command line:
- ``python masterdata_checker.py``

From Jupyter Notebooks:
- ``jupyter-notebook`` (on the command line)
- Open the file *jupyter_checker/checker_jupyter.ipynb*



## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
