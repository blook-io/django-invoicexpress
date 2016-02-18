#-*- coding:utf-8 -*-
import re

import requests
import xmltodict

from django.conf import settings
from requests import Request, Session



from . import api

### CONFIG ###






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



def ask_api(method, xml_params={}, url_params={}):
	""" this function will do all  requests 
		to Invocexpress API

	:param action: 			api call name (e.g. users.accouts , invoices.get)
	:param xml_params: 	params, that should specified in xml body long list of additional arguments;
	:param url_params: 	params, that is part of url;

	:returns:		API answer as python dict 
	"""

	action = api.method[method]

	# find all params in brackets
	keys_in_url = re.findall('\{(.[^\}]+)\}',action['url'])

	addr_params = {}
	for key in keys_in_url:
		if key in url_params:
			addr_params[key] = url_params[key]
			del url_params[key]

	addr_params['account-name'] = settings.INVOICE_EXPRESS_ACCOUNT_NAME

	# now compile urls using settings
	url = action['url'].format(**addr_params)

	headers = {'Content-Type': 'application/xml'}
	url_params['api_key'] = settings.INVOICE_EXPRESS_API_KEY

	request_args = {}
	if xml_params != {} :
		# wrap xml_params in root_tag
		xml_params = { api.root_tag_name(method): xml_params }
		request_args['data'] = xmltodict.unparse(xml_params)
		
	print url
	print headers
	print url_params
	print request_args
	#TODO: use one session for many requests
	s = Session()
	req = Request( action['method'],
		url = url,
	    headers=headers,
	    params = url_params,
	    **request_args
	)
	prepared = req.prepare()
	# TODO: connection error handling
	resp = s.send(prepared)

	print resp

	if resp.status_code == 200 or resp.status_code==201:
		try :
			out  = xmltodict.parse(resp.text)
		except:
			out = resp.text
		return out 
	else :
		raise api.ApiCallError( str(resp.status_code)+': '+resp.text )
	# else:
	# 	raise api.ApiCallError( xmltodict.parse(resp.text) )




