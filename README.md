# Masterdata Checker

The `masterdata_checker` is a Django app used to check the correctness of a given Masterdata definitions file with respect to the entities already registered in the BAM Data Store (as defined in the [`bam-masterdata`](https://github.com/BAMresearch/bam-masterdata) package). In the app, you can:
- Log in your openBIS instance.
- Run checks of a local Masterdata Excel file. **Note**: only supported file formats are `.xls` and `.xlsx`
- Revise the errors logs to correct mistakes in the original Masterdata file.


## Development

If you want to develop locally this package, clone the project and enter in the workspace folder:
```sh
git clone https://github.com/BAMresearch/masterdata-checker
cd masterdata_checker
```

We recommend using `uv` for fast pip installation of the package. In this case, you can instead create a virtual environment by doing:
```sh
uv venv
source .venv/bin/activate
```

Install the package with the desired optional dependencies (specified in between brackets, e.g., `[dev]`) and in editable mode (with the added `-e` flag):
```sh
uv pip install -e '.[dev]'
```

### Launch the Django app

In order to launch the Django app, navigate to the `masterdata_checker/` subfolder:
```sh
cd masterdata_checker
```

And run:
```sh
python manage.py runserver
```

This will run the Django app server:
```sh
Performing system checks...

System check identified no issues (0 silenced).
June 05, 2025 - 06:24:20
Django version 5.2.1, using settings 'checker.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Simply click on the localhost address `http://127.0.0.1:8000/` to launch the app.


## Main contributors

| Name | E-mail     | Role |
|------|------------|--------|
| Carlos Madariaga | [carlos.madariaga@bam.de](carlos.madariaga@bam.de) | Admin |
| Dr. Jose M. Pizarro | [jose.pizarro-blanco@bam.de](jose.pizarro-blanco@bam.de) | Maintainer |
| Jörg Rädler | [joerg.raedler@bam.de](joerg.raedler@bam.de) | Maintainer |
| Dr. Angela Ariza | [angela.ariza@bam.de](angela.ariza@bam.de) | Maintainer |
