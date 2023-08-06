import click
import subprocess
import os


@click.command(name='status')
def status():
    """
    Checks the status of the Vectordash client.
    """
    # note that supervisor prints a message, so we don't need to print one ourselves
    subprocess.call("sudo supervisorctl status vdhost", shell=True)
