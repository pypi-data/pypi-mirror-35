Webfaction fabric2 helper scripts
=================================

These scripts utilise the `Webfaction
API <https://docs.webfaction.com/xmlrpc-api/>`__ via python and `Fabric
2 <http://www.fabfile.org/>`__ to conveniently run some common tasks.

Presently there are just a small selection, mostly related to managing
letsencrypt certificates.

Installation
------------

You could install this in your system python3, into your virtualnv or
into your pipenv as a dev dependency

   $ pipenv install –dev webfaction_fab2

Usage
-----

Generate a fabfile.py in the root of your project, something like this:

   $ pipen run python -m wf_fab2.makefab

And then start using the commands

   $ pipenv run fab -l

::

    Loading .env environment variables...
   Available tasks:

   Available tasks:

     acme-install     Install acme.sh for Letsencrypt certificates on a webfaction host.
     check-websites   Check http response mode of all configured websites.
     list-websites    List all websites their linked apps and subdomains.
     secure-website   Issue certificates for a website and install with acme_webfaction

..

   $ pipenv run fab -H Web39.webfaction.com check-websites accountname

::

   Loading .env environment variables...
   API password:
   Checking: https://example.com/
   Available: https://example.com/
   Checking: https://anotherexample.com/
   /Users/mjoakes/.local/share/virtualenvs/webfaction_helpers-RUB6JD7n/lib/python3.6/site-packages/urllib3/connectionpool.py:857: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
     InsecureRequestWarning)
   Available: https://anotherexample.com/ Invalid Certificate

..

   $ pipenv run fab -H Web39.webfaction.com list-websites accountname

::

   API password:
   example_site_name [['exampleapp', '/']] ['example.com', 'www.example.com']
   anotherexample_site_name [['anotherexampleapp', '/']] ['anotherexample.com', 'www.anotherexample.com']

..

   $ pipenv run fab -H Web39.webfaction.com ssecure-website accountname
   anotherexample_site_name

::

Development
-----------

I had a pretty comprehensive and well tested set of scripts for fabric
1.x enabling provisioning and deploying django projects onto webfaciton
hosts. As I slowly move them to fabric2 I’m intending to share them
here.

https://github.com/moaxey/wf_fab2
