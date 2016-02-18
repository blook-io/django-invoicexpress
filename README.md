# django-invoicexpress
Django-invocexpress -  Python implementation of Invocexpress (https://invoicexpress.com) API

Installation
=================

1. Go to blook project root ( :) )
2. git clone ssh://git@github.com:blook-io/django_invoicexpress.git
3. pip install -r django_invoicexpress/requirements.txt 

Options
-----------------
settings.INVOICE_EXPRESS_ACCOUNT_NAME :
	Account name from invoicexpress.com

settings.INVOICE_EXPRESS_API_KEY :
	API key from invoicexpress.com


How to make calls? By specifying all needed parameters (except API_KEY, which is in settings);

Using
-----------------

export DJANGO_SETTINGS_MODULE='your_project.settings'

python -m django_invoicexpress.test

Notes
---------------------

- potentially  Module can be used for any python framwork (with minor changes for other frameworks)  
