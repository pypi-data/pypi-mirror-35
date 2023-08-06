import click
import subprocess


@click.command(name='run-tests')
def run_tests():
    """
    Runs the host tests post-installation.
    This is simply a wrapper around host_tests.pyc.
    """
    subprocess.call("python3 /var/vectordash/client/host_tests.pyc", shell=True)

