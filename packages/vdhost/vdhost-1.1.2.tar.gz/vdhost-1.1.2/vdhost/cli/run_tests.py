import click
import subprocess
import os

from colored import fg
from colored import stylize


@click.command(name='run-tests')
def run_tests():
    """
    Runs the host tests post-installation.
    This is simply a wrapper around host_tests.pyc.
    """

    # if the installation has not been completed
    if not os.path.isfile('/var/vectordash/flags/installation_complete'):
        print("The Vectordash client has not been installed. Please run " +
              stylize("sudo vdhost install", fg("blue")))
        return

    # running the test suite
    subprocess.call("python3 /var/vectordash/client/host_tests.pyc", shell=True)

