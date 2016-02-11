import requests
import xmltodict

from django.conf import settings
from requests import Request, Session

from . import api

### CONFIG ###

# temporarily this will be here, not in actual settings
settings.INVOICE_EXPRESS_ACCOUNT_NAME = 'blookpt'
settings.INVOICE_EXPRESS_API_KEY = 'b761e9c48d58d5ccd2950a4aa22f3ac5876fc6b0'




# enspired by http://stackoverflow.com/questions/30259452/proper-way-to-consume-data-from-restful-api-in-django
# def get_books(year, author):
#     url = 'http://api.example.com/books' 
#     params = {'year': year, 'author': author}
#     r = requests.get('http://api.example.com/books', params)
#     books = r.json()
#     books_list = {'books':books['results']}

# xml = """<?xml version='1.0' encoding='utf-8'?>
# <a>б</a>"""
# headers = {'Content-Type': 'application/xml'} # set what your server accepts
# print requests.post('http://httpbin.org/post', data=xml, headers=headers).text

context = {
	'account_name': settings.INVOICE_EXPRESS_ACCOUNT_NAME,
}



def ask_api(action, **kw):
	""" this function will do all  requests 
		to Invocexpress API

	:param action: 	api call name (e.g. users.accouts , invoices.get)
	:param kw: 		long list of additional arguments;
					ATTENTION - all parameters will be sended as XML

	:returns:		API answer as python dict 
	"""

	action = api.method[action]

	# now compile urls using settings
	url = action['url'].format(**context)
	headers = {'Content-Type': 'application/xml'}

	#TODO: use one session for many requests
	s = Session()
	
	req = Request( action['method'],
	    headers=headers,
	    data=xmltodict.unparse(**kw),
	)
	# TODO: connection error handling
	resp = s.send(req)

	if resp.status_code == 200:
		return xmltodict.parse(resp.text)
	else:
		# Ohh, what is wrong ??
		return {}
	# print(resp.status_code)




