# django-invoicexpress
Django-invocexpress -  Python implementation of Invocexpress (https://invoicexpress.com) API

Using in Django Projects
------------------------
1. Clone to folder with name `invoicexpress`
	
	git clone https://github.com/blook-io/django-invoicexpress.git invoicexpress

2. in settings.py

	INVOICE_EXPRESS_ACCOUNT_NAME = 'your_account_name'
	
	INVOICE_EXPRESS_API_KEY  = 'your_api_key'

Running Tests
------------------

1. export DJANGO_MODULE_SETTINGS='your.app.settings'
2. python -m invoicexpress.test

Docs
------------------
http://django-invoicexpress.readthedocs.org/en/latest/



