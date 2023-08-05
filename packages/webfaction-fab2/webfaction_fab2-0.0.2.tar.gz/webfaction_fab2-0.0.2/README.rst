Commands to invoke in webfaction servers.
=========================================

Scripts to assist in deploying and maintain web sites on Webfaction servers.

Based on [Fabric 2.0](http://www.fabfile.org/) and Webfaction's [xmlrpc API](https://docs.webfaction.com/xmlrpc-api/) version 2.


Account and server level tasks
------------------------------

Generating Letsencrypt SSL certificates with [acme.sh](https://github.com/Neilpang/acme.sh) using [dns manual mode](https://github.com/Neilpang/acme.sh/wiki/dns-manual-mode)

#. install_acme

   * Installs acme.sh in a Webfaction account

#. uninstall_acme

   * Installs acme.sh from a Webfaction account. Certificates are left.

#. secure_domains
   
   * Validates domains with DNS manual mode,
   * generates a certificate under the primary domain for all the domains and
   * installs it.

#. check websites
   
   * Attempts to load all the accounts configured websites and
   * reports their HTTP response codes


Website level tasks
-------------------

#. django_update
#. check_secure_versions
#. provision
#. teardown
#. deploy
