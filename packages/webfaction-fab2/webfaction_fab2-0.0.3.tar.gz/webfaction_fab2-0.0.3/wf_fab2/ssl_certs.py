#!/usr/bin/env python
import re
import os
import logging
import time
import dns.resolver
from io import StringIO
from .util import ensure_webfaction


def install_acme_webfaction(c):
    """ Install acme.sh and acme_webfaction.py on a host """
    logging.debug('install_acme')
    home = c.run("echo $HOME").stdout.strip()
    c.run(f"mkdir -p {home}/src {home}/bin")
    with c.cd(f"{home}/src"):
        c.run("curl https://get.acme.sh | sh")
        c.run("rm master.zip", warn=True)
        c.run("wget https://github.com/gregplaysguitar/acme-webfaction/archive/master.zip")
        c.run("unzip master.zip")
        c.run("rm master.zip")
        c.run(f"cp acme-webfaction-master/acme_webfaction.py {home}/bin")
        c.run("rm -r acme-webfaction-master")
    c.run(f"chmod +x {home}/bin/acme_webfaction.py")


def cert_issue_install_renew(
        c,
        server,
        session_id,
        account,
        machine,
        website_name,
        password,
        force=False
):
    """ Issue a certificate for a website and set up auto renewal. """
    # vaidate web_site_name, find the path to the app at /
    home = c.run("echo $HOME").stdout.strip()
    website_details = get_website_details(server, session_id, website_name)
    root_app_name = [
        a[0] for a in website_details['website_apps'] if a[1] == '/'
    ][0]
    apps = server.list_apps(session_id)
    root_app_details = [a for a in apps if a['name'] == root_app_name][0]
    if re.match(r'(django|rails)', root_app_details['type']):
        acme_web_root = f"{home}/temp"
        c.run(f"mkdir -p {acme_web_root}")
        configure_apache_for_alias(c, root_app_name, home)
    else:
        acme_web_root = f"{home}/webapps/{root_app_name}"
    sorted_domains = sorted(website_details['subdomains'], key=len)
    domain_args = get_domain_args(sorted_domains)
    do_force = "--force" if force else ""
    installation_transcript = c.run((
        f"{home}/.acme.sh/acme.sh --issue {do_force} -w '{acme_web_root}' "
        f"{domain_args}"
    ), warn=True).stdout
    certificate_detail = api_install_cert(
        c, server, session_id, *sorted_domains
    )
    acme_install_renew(
        c, server, session_id, account, machine, password, sorted_domains
    )

def get_domain_args(sorted_domains):
    return "-d " + " -d ".join(sorted_domains)


def get_cert_name(server, session_id, sorted_domains):
    certs = server.list_certificates(session_id)
    for cert in certs:
        if cert['domains'] == ','.join(sorted_domains):
            return cert['name']
    raise ValueError('No certificate found for domains: {domain_args}')


def acme_install_renew(
        c, server, session_id, account, machine, password, sorted_domains
):
    home = c.run("echo $HOME").stdout.strip()
    domain_args = get_domain_args(sorted_domains)
    cert_name = get_cert_name(server, session_id, sorted_domains)
    reloadcmd = f"WF_SERVER='{machine}' WF_USER='{account}' WF_PASSWORD='{password}'  WF_CERT_NAME='{cert_name}' {home}/bin/acme_webfaction.py"
    c.run(f"{home}/.acme.sh/acme.sh --install-cert {domain_args} --reloadcmd \"{reloadcmd}\"")


def configure_apache_for_alias(c, root_app_name, home):
    root_app_dir = f"{home}/webapps/{root_app_name}"
    remote_httpd_conf = f"{root_app_dir}/apache2/conf/httpd.conf"
    httpd_conf = c.run(
        f"cat '{remote_httpd_conf}'"
    ).stdout.strip()
    load_module = 'LoadModule alias_module      modules/mod_alias.so'
    well_known_alias = f"Alias /.well-known/ {home}/temp/.well-known/"
    httpd_conf = apache_conf_insert(httpd_conf, load_module)
    httpd_conf = apache_conf_insert(httpd_conf, well_known_alias)
    httpd_conf_file = StringIO(httpd_conf)
    c.put(httpd_conf_file, remote_httpd_conf)
    c.run(f"{root_app_dir}/apache2/bin/restart")


def get_website_details(server, session_id, website_name):
    websites = server.list_websites(session_id)
    website_names = [s['name'] for s in websites]
    if website_name not in website_names:
        raise ValueError(
            "Unrecognised website name. Available websites are: {}".format(
                ', '.join(website_names)
            )
        )
    return [w for w in websites if w['name'] == website_name][0]


def apache_conf_insert(conf, line):
    """ Crudely add apache directives near other similar directives. """
    sections = conf.split('\n\n')
    directive, value = line.split(' ', 1)
    added = False
    for scount in range(len(sections)):
        if sections[scount].find(directive) >= 0:
            if sections[scount].find(line) < 0:
                sections[scount] += '\n' + line
            added = True
            break
    if not added:
        sections.append(line)
    return '\n\n'.join(sections)


def api_install_cert(c, server, session_id, *sorted_domains):
    logging.debug('install_certificate')
    primary_domain = sorted_domains[0]
    certfolder = os.path.join('.acme.sh', primary_domain)
    certificate = str(
        c.run(
            'cat "{}"'.format(
                os.path.join(certfolder, f'{primary_domain}.cer')
            )
        ).stdout
    )
    private_key = str(
        c.run(
            'cat "{}"'.format(
                os.path.join(certfolder, f'{primary_domain}.key')
            )
        ).stdout
    )
    intermediates = str(
        c.run(
            'cat "{}"'.format(
                os.path.join(certfolder, 'fullchain.cer')
            )
        ).stdout
    )
    cert_name = get_cert_name(server, session_id, sorted_domains)
    resp = create_or_update_certificate(
        server,
        session_id,
        primary_domain,
        cert_name,
        certificate,
        private_key,
        intermediates,
    )
    return resp

def create_or_update_certificate(
        server,
        session_id,
        primary_domain,
        cert_name,
        certificate,
        private_key,
        intermediates,
        ):
    logging.debug('create_or_update_certificate')
    current_certificates = server.list_certificates(session_id)
    for ccert in current_certificates:
        if ccert['name'] == cert_name:
            return server.update_certificate(
                session_id,
                cert_name,
                certificate,
                private_key,
                intermediates,
            )
    return server.create_certificate(
        session_id,
        cert_name,
        certificate,
        private_key,
        intermediates,
    )

def create_dns_override(
        server,
        session_id,
        domain,
        a_ip,
        cname,
        mx_name,
        mx_priority,
        spf_record,
        aaaa_ip,
        srv_record
):
    logging.debug('create_dns_override')
    result = server.create_dns_override(
        session_id,
        domain,
        a_ip,
        cname,
        mx_name,
        mx_priority,
        spf_record,
        aaaa_ip,
        srv_record
    )
    return result


def delete_dns_override(
        server,
        session_id,
        domain,
        a_ip,
        cname,
        mx_name,
        mx_priority,
        spf_record,
        aaaa_ip,
        srv_record
):
    logging.debug('delete_dns_override')
    result = server.delete_dns_override(
        session_id,
        domain,
        a_ip,
        cname,
        mx_name,
        mx_priority,
        spf_record,
        aaaa_ip,
        srv_record
    )
    return result


def create_domain(
        server,
        session_id,
        domain_name,
        *subdomains
):
    logging.debug('create_domain')
    result = server.create_domain(
        session_id,
        domain_name,
        *subdomains
    )
    return result


def delete_domain(
        server,
        session_id,
        domain,
        *subdomains
):
    logging.debug('delete_domain')
    try:
        return server.delete_domain(session_id, domain, *subdomains)
    except Fault as e:
        logging.error(e)



