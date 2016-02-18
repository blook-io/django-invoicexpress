# ??? dont know what is API version 

class ApiCallError(Exception):
	pass

def root_tag_name(method) :
	if method[:6]=='client' :
		return 'client'

method = {

	'user.accounts' : {
		'url'		: 'https://www.app.invoicexpress.com/users/accounts.xml',
		'method' 	: 'GET',
	},

	'user.change-account' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/users/change_account.xml',
		'method' 	: 'POST',
	},

	# Clients

	'clients.create' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients.xml',
		'method' 	: 'POST',
		},
	'clients.get' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/{client-id}.xml',
		'method' 	: 'GET',
		},
	'clients.update' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/{client-id}.xml',
		'method'	: 'PUT',
		},
	'clients.list' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients.xml',
		'method'	: 'GET',
		},
	'clients.invoices' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/{client-id}/invoices.xml',
		'method'	: 'GET',
		},
	'clients.find-by-name' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/find-by-name.xml',
		'method'	: 'GET',
		},
	'clients.find-by-code' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/find-by-code.xml',
		'method'	: 'GET',
		},
	'clients.create-invoice' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/{client-id}/create/invoice.xml',
		'method'	: 'POST',
		},
	'clients.create-credit-note' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/{client-id}/create/credit-note.xml',
		'method'	: 'POST',
		},
	'clients.create-debit-note' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/{client-id}/create/debit-note.xml',
		'method'	: 'POST',
		},
}