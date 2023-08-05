import os
from hs.admin.api import API
import hsutilities.users as hsusers

def get_api(username=None, password=None):

    if not username:
        username = hsusers.get_current_pac()
    if not password:
        # read password from home directory
        filename = os.path.join(os.path.expanduser("~"), ".hsadmin.properties")
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                #xyz00.passWord=topsecret
                if line.startswith(f"{username}.passWord="):
                    password = line[len(f"{username}.passWord="):].strip()

    api = API(cas={'uri': 'https://login.hostsharing.net/cas/v1/tickets',
                   'service': 'https://config.hostsharing.net:443/hsar/backend'},
              credentials={'username': username, 'password': password},
              backends=['https://config.hostsharing.net:443/hsar/xmlrpc/hsadmin',
                        'https://config2.hostsharing.net:443/hsar/xmlrpc/hsadmin'])
    return api

