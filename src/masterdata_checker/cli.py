import getpass

import click
from pybis import Openbis

# from masterdata_checker.main import start_gui


@click.group(
    help=(
        'This is the entry point of the `masterdata_checker` Command Line Interface (CLI). '
        'Please, use `--help` at any moment to show the possible options.'
    )
)
def cli():
    """CLI for launching the masterdata_checker GUI."""
    pass


@cli.command()
@click.argument('username')
@click.argument('instance')
def masterdata_checker(username: str, instance: str = 'main'):
    password = getpass.getpass(prompt='Please enter your password: ')
    url = f'https://{instance}.datastore.bam.de/'
    print(username, instance, password)
    # o = Openbis(url)
    # o.login(username, password, save_token=True)

    # o.logout()

    # start_gui(o, instance)  # Call the tkinter GUI


if __name__ == '__main__':
    cli()
