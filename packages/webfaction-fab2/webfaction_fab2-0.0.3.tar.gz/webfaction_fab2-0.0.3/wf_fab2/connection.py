from xmlrpc.client import ServerProxy
from getpass import getpass


def start_session(account, machine, password=None):
    """ returns server and session_id for reuse in API calls """
    server = ServerProxy(
        'https://api.webfaction.com/',
    )
    if password is None:
        password = getpass('API password: ')
    session_id, returned_account = server.login(
        account, password, machine, 2,
    )
    return server, session_id
