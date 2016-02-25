Invoice Receipt
----------------

In general all aprameters to `ask_api` are filled according to InvoiceXpress API docs. But there are some simplifications.

invoice-receipts.create
*****************************

Api docs: https://invoicexpress.com/api/invoice-receipt

Specify `items` as simple list. 

Example:

.. code-block:: python 

	result = ask_api('invoice-receipts.create', { 
		'date': '01/01/2014',
		'due_date': '01/02/2014',
		'client' : {
			'name' : 'Ricardo Pereira',
			'code' : 100,
		},
		'items' : [
			{	
				'name' : 'Product 1',
				'description' : "Cleaning product",
				'unit_price': 12.0,
				'quantity' : 2.0,
			},
			{	
				'name' : 'Product 2',
				'description' : "Beauty product",
				'unit_price': 123.0,
				'quantity' : 1.0,
			},
		],
				
			
	})

	#print some fields 
	print 'ID:', result['id'] 
	print 'Link:', result['permalink']


invoice-receipts.get
************************

Api docs: https://invoicexpress.com/api/invoice-receipt/get

Example:

.. code-block:: python
	
	receipt = ask_api('invoice-receipts.get', {
		'invoice-receipt-id' : your_id 	
	})
	
	# print fields
	print receipt['permalink']


invoice-receipts.update
***************************
Api docs: https://invoicexpress.com/api/invoice-receipt/update

Example:

.. code-block:: python
	
	# suggest you get receipt as above
	
	# now we will change client
	ask_api('invoice-receipts.update', {
		'invoice-receipt-id': receipt['id'],
		'due_date': receipt['due_date'],
		'date': receipt['date'],
		'client' : {
			'name' : 'Ricardo Ferrera',
			'code' : '122'
		},
		'items' : receipt['items']
	})

invoice-receipts.list
*****************************
Api docs: https://invoicexpress.com/api/invoice-receipt/list

Example:

.. code-block:: python

	result = ask_api('invoice-receipts.list', {
			'per_page': 7,
			'page' : 1
			})

	print "Current page:" , result['current_page']

	for r in result['invoice_receipt']:
		print (
			'Id: {} Client: {}'.format (r['id'],r['client']['name']) 
		)


invoice-receipts.change-state
*********************************
Api docs: https://invoicexpress.com/api/invoice-receipt/change-state

**Note**: Bug in API docs, you must write `finalized` instead `settled` 

Example:

.. code-block:: python

	# make finalize
	result = ask_api('invoice-receipts.change-state', {
			'invoice-receipt-id': receipt['id'],
			'state': 'finalized',
		})

	print result


invoice-receipts.email-document
************************************
Api docs: https://invoicexpress.com/api/invoice-receipt/email

**Note**: Вody is Plain text 

Example:

.. code-block:: python


	result = ask_api('invoice-receipts.email-document', {
		'invoice-receipt-id': your_receipt['id'],

		'client': {
			'email': 'example@mail.pt',
			'save': 0,
		},

		'subject' : 'The Html Letter',
		'body' : 'Will be printed as <b> Plain </b> text'
	})


invoice-receipts.related_documents
*****************************************
Api docs: https://invoicexpress.com/api/invoice-receipt/related-documents

Example:

.. code-block:: python


	result = ask_api('invoice-receipts.related_documents', {
			'invoice-receipt-id' : a['id']
	})


TODO: add example of printing results





