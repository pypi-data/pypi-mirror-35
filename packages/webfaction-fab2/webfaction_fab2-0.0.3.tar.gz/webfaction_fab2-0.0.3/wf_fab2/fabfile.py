#!/usr/bin/env python
from fabric import task
import os
import logging
from getpass import getpass
from wf_fab2.util import ensure_webfaction, is_dir
from wf_fab2.connection import start_session
from wf_fab2.websites import website_checker
from wf_fab2.ssl_certs import (
    install_acme_webfaction, cert_issue_install_renew, acme_install_renew
)

logging.basicConfig(
    filename=os.path.join(
        os.path.dirname(
            os.path.realpath(__file__)
        ),
        'fab.log'
    ),
    level=logging.DEBUG
)


@task
def acme_install(c, account):
    """ Install acme.sh for Letsencrypt certificates on a webfaction host. """
    machine = ensure_webfaction(c)
    server, session_id = start_session(account, machine)
    install_acme_webfaction(c)


@task(optional=['force'])
def secure_website(
        c,
        account,
        website_name,
        force=None,
):
    """ Issue certificates for a website and install with acme_webfaction """
    machine = ensure_webfaction(c)
    password = getpass('API password: ')
    server, session_id = start_session(account, machine, password)
    primary_domain = cert_issue_install_renew(
        c, server, session_id, account, machine, website_name, password, force
    )


def acme_renew(c, account, domains):
    """ Run the renewal process for existing certs based on domains. """
    machine = ensure_webfaction(c)
    password = getpass('API password: ')
    server, session_id = start_session(account, machine, password)
    sorted_domains = sorted(domains.split(','), key=len)
    acme_install_renew(
        c, server, session_id, account, machine, password, sorted_domains
    )


@task
def list_websites(
        c,
        account,
):
    """ List all websites their linked apps and subdomains. """
    machine = ensure_webfaction(c)
    server, session_id = start_session(account, machine)
    for site in server.list_websites(session_id):
        print(site['name'], site['website_apps'], site['subdomains'])


@task
def check_websites(
        c,
        account,
):
    """ Check http response mode of all configured websites. """
    machine = ensure_webfaction(c)
    server, session_id = start_session(account, machine)
    website_checker(server, session_id, machine)
