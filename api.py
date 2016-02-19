# ??? dont know what is API version 

from . import errors 



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
		'root_tag_name' : 'client',
		},
	'clients.get' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/{client-id}.xml',
		'method' 	: 'GET',
		},
	'clients.update' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/{client-id}.xml',
		'method'	: 'PUT',
		'root_tag_name' : 'client',
		},
	'clients.list' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients.xml',
		'method'	: 'GET',
		'root_tag_name' : 'client',
		},
	'clients.invoices' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/{client-id}/invoices.xml',
		'method'	: 'GET',
		'root_tag_name' : 'filter',
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
		'root_tag_name' : 'invoice',
		},
	'clients.create-credit-note' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/{client-id}/create/credit-note.xml',
		'method'	: 'POST',
		'root_tag_name' : 'credit_note',
		},
	'clients.create-debit-note' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/clients/{client-id}/create/debit-note.xml',
		'method'	: 'POST',
		'root_tag_name' : 'debit_note',
		},

	# invoice_receipt

	'invoice-receipts.create' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/invoice_receipts.xml',
		'method'	: 'POST',
		'root_tag_name' : 'invoice_receipt',
		},
	'invoice-receipts.get' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/invoice_receipts/{invoice-receipt-id}.xml',
		'method'	: 'GET',
		},
	'invoice-receipts.update' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/invoice_receipts/{invoice-receipt-id}.xml',
		'method'	: 'PUT',
		'root_tag_name' : 'invoice_receipt',
		},
	'invoice-receipts.list' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/invoice_receipts.xml',
		'method'	: 'GET',
		'root_tag_name' : 'invoice_receipt',
		},
	'invoice-receipts.change-state' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/invoice_receipts/{invoice-receipt-id}/change-state.xml',
		'method'	: 'PUT',
		'root_tag_name' : 'invoice_receipt',
		},
	'invoice-receipts.email-document' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/invoice_receipts/{invoice-receipt-id}/email-document.xml',
		'method'	: 'PUT',
		'root_tag_name' : 'message',
		},
	'invoice-receipts.related_documents' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/document/{invoice-receipt-id}/related_documents.xml',
		'method'	: 'GET',
		},
	'invoice-receipts.pdf' : {
		'url'		: 'https://{account-name}.app.invoicexpress.com/api/pdf/{invoice-receipt-id}.xml',
		'method'	: 'GET',
		},

}