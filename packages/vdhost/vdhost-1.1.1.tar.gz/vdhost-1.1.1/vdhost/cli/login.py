import click
import os
import json
import requests
from requests.compat import urljoin
from colored import fg
from colored import stylize
from os import environ

if environ.get('VECTORDASH_BASE_URL'):
    VECTORDASH_URL = environ.get('VECTORDASH_BASE_URL')
    print('Using development URL:' + VECTORDASH_URL)
else:
    VECTORDASH_URL = "https://vectordash.com/"


@click.command(name='login')
def login():
    """
    Login with your Vectordash credentials.
    """
    try:
        # Path to vectordash directory
        var_folder = '/var/'
        var_vd_folder = var_folder + 'vectordash/'
        client_vd_folder = var_vd_folder + 'client/'

        # If the var directory does not exist, create it
        if not os.path.isdir(var_folder):
            os.mkdir(var_folder)

        # If the vectordash directory does not exist, create it
        if not os.path.isdir(var_vd_folder):
            os.mkdir(var_vd_folder)

        # If the client directory does not exist, create it
        if not os.path.isdir(client_vd_folder):
            os.mkdir(client_vd_folder)

        # Ask user for email address
        email = input(stylize("Email: ", fg("blue")))

        # Asking the user for machine key
        machine_key = input(stylize("Machine secret: ", fg("blue")))

        # POSTing their credentials
        data = {'email': email, 'machine_key': machine_key}
        r = requests.post(urljoin(VECTORDASH_URL, "authenticate-host/"), data)
        r.raise_for_status()

        resp = r.text
        resp = json.loads(resp)

        # if the authentication info is invalid
        if not resp['valid_authentication']:
            print(stylize("Your authentication information is invalid.", fg("red")))
            return

        # login credentials
        login_file = os.path.join('/var/vectordash/login.json')

        # Writing the credentials to login.json
        with open(login_file, 'w') as f:
            data = {'email': email, 'machine_key': machine_key}
            json.dump(data, f)
            print(stylize("Login information saved.", fg("green")))
            return

    except OSError:
        print(stylize("Could not save login credentials. Please run ", fg("red"))
              + stylize("sudo vdhost login", fg("blue")))
        
    except Exception as e:
        print(stylize("The following error was encountered: ", fg("red")) + str(e))
