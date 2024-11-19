# BAM Data Store: MasterDataChecker

The `masterdata_checker` is a Python package used to check the correctness of a given Masterdata definitions file with respect to the entities already registered in the BAM Data Store. The package provides a Graphical User Interface (GUI) on which the user can:
- Choose a local Masterdata file to be checked.
- Revise the errors logs to correct mistakes in the original Masterdata file.
- Depending on the credentials access, select a specific BAM Data Store instance and the Masterdata definitions therein.

We also provide a Jupyter Notebook as a tutorial to execute the API of `masterdata_checker`.


<!--
## Getting started

 Add here installation instructions once the package is deployed -->

## Development

If you want to develop locally this package, clone the project and enter in the workspace folder:
```sh
git clone https://git.bam.de/bam-data-store/development/masterdata_checker.git
cd masterdata_checker
```

Note you need to have installed the Python interface for the Tcl/Tk GUI toolkit ([`tkinter`](https://docs.python.org/3/library/tkinter.html)). If you don't have it, you can run:
```sh
sudo apt-get install python3-tk
```

#### Option 1: Virtual environment with `venv`

Create a virtual environment (you can use Python>3.9) in your workspace:
```sh
python3 -m venv .venv
source .venv/bin/activate
```

Make sure `pip` is upgraded:
```sh
pip install --upgrade pip
```

Install the package with the desired optional dependencies (specified in between brackets, e.g., `[dev]` or `[jupy]`) and in editable mode (with the added `-e` flag):
```sh
pip install -e '.[dev,jupy,docu]'
```

#### Option 2: `uv` virtual environment

We recommend using `uv` for fast pip installation of the package. In this case, you can instead create a virtual environment by doing:
```sh
uv venv
source .venv/bin/activate
```

Install the package with the desired optional dependencies (specified in between brackets, e.g., `[dev]` or `[jupy]`) and in editable mode (with the added `-e` flag):
```sh
uv pip install -e '.[dev,jupy,docu]'
```

### Run the tests

You can locally run the tests by doing:
```sh
python -m pytest -sv tests
```

where the `-s` and `-v` options toggle the output verbosity.

You can also generate a local coverage report:
```sh
python -m pytest --cov=src tests
```

### Run auto-formatting and linting

We use [Ruff](https://docs.astral.sh/ruff/) for formatting and linting the code following the rules specified in the `pyproject.toml`. You can run locally:
```sh
ruff check .
```

This will produce an output with the specific issues found. In order to auto-fix them, run:
```sh
ruff format . --check
```

If some issues are not possible to fix automatically, you will need to visit the file and fix them by hand.

<!-- ### Debugging

For interactive debugging of the tests, use `pytest` with the `--pdb` flag. We recommend using an IDE for debugging, e.g., _VSCode_. If that is the case, add the following snippet to your `.vscode/launch.json`:
```json
{
  "configurations": [
      {
        "name": "<descriptive tag>",
        "type": "debugpy",
        "request": "launch",
        "cwd": "${workspaceFolder}",
        "program": "${workspaceFolder}/.pyenv/bin/pytest",
        "justMyCode": true,
        "env": {
            "_PYTEST_RAISE": "1"
        },
        "args": [
            "-sv",
            "--pdb",
            "<path-to-plugin-tests>",
        ]
    }
  ]
}
```

where `<path-to-plugin-tests>` must be changed to the local path to the test module to be debugged.

The settings configuration file `.vscode/settings.json` automatically applies the linting and formatting upon saving the modified file. -->

### Documentation on Github pages

To view the documentation locally, install the extra packages using:
```sh
uv pip install -e '[docu]'
```

The first time, build the server:
```sh
mkdocs build
```

Run the documentation server:
```sh
mkdocs serve
```

The output looks like:
```sh
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  [14:07:47] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [14:07:47] Serving on http://127.0.0.1:8000/
```

Simply click on `http://127.0.0.1:8000/`. The changes in the `md` files of the documentation are inmediately reflected when the files are saved (the local web will automatically refresh).

## Main contributors

| Name | E-mail     | Role |
|------|------------|--------|-----------------|
| Carlos Madariaga | [carlos.madariaga@bam.de](carlos.madariaga@bam.de) | Admin |
| Dr. Jose M. Pizarro | [jose.pizarro-blanco@bam.de](jose.pizarro-blanco@bam.de) | Maintainer |
| Jörg Rädler | [joerg.raedler@bam.de](joerg.raedler@bam.de) | Maintainer |
| Dr. Angela Ariza | [angela.ariza@bam.de](angela.ariza@bam.de) | Maintainer |
