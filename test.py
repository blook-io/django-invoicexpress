import unittest


import uuid
from services import  ask_api

from . import errors

class ClientsApi(unittest.TestCase):
	def test_crud(self):
		
		result = ask_api('clients.create', { 
				'name': 'Pedro', 
				'code': uuid.uuid4(),
		})
		self.assertTrue( 'client' in result )
		self.assertEqual( 'Pedro', result['client']['name'] )

		new_user_id = result['client']['id']
		print new_user_id

		# Listing all users
		result = ask_api('clients.list',{
			'per_page': 50,
			})
		print result
		self.assertTrue( 'clients' in result)

		# search for new user
		# find_it = False
		# for u in result['clients']['client']:
		# 	print u['id']
		# 	if u['id'] == new_user_id:
		# 		find_it = True
		# self.assertTrue ( find_it )


		# updating user
		result = ask_api('clients.update',{
					'name' : "Adam",
			},
			url_params={
				'client-id' : new_user_id,
			}
		)

		print "Update result: ", result

		# searching for new

		# for u in result['clients']['client']:
			# print "ID: {id}, Name: {name}, Code: {code}".format(**u)


class InvoiceReceiptsApi(unittest.TestCase):
	# def test_crud(self):
	# 	# imitate error 422
	# 	with self.assertRaises(errors.ApiCallError):

	# 		result = ask_api('invoice-receipts.create', { 
	# 				'date': '01/01/2014',
	# 				'due_date': '01/02/2014',
	# 				'client' : {
	# 					'name' : 'Ricardo Pereira',
	# 					'code' : 100,
	# 				},
	# 				'items' : [
	# 					{	
	# 						'name' : 'Product 1',
	# 						'description' : "Cleaning product",
	# 						'unit_price': 12.0,
	# 						'quantity' : 2.0,
	# 					},
	# 					{	
	# 						'name' : 'Product 2',
	# 						'description' : "Beauty product",
	# 						'unit_price': 123.0,
	# 						'quantity' : 'bla bla',
	# 					},
	# 				],
						
					
	# 		})
	# 	# now get normall call
	# 	result = ask_api('invoice-receipts.create', { 
	# 		'date': '01/01/2014',
	# 		'due_date': '01/02/2014',
	# 		'client' : {
	# 			'name' : 'Ricardo Pereira',
	# 			'code' : 100,
	# 		},
	# 		'items' : [
	# 			{	
	# 				'name' : 'Product 1',
	# 				'description' : "Cleaning product",
	# 				'unit_price': 12.0,
	# 				'quantity' : 2.0,
	# 			},
	# 			{	
	# 				'name' : 'Product 2',
	# 				'description' : "Beauty product",
	# 				'unit_price': 123.0,
	# 				'quantity' : 1.0,
	# 			},
	# 		],
					
				
	# 	})
	# 	print 'ID:', result['id'] 
	# 	print 'Link:', result['permalink'] 
		
	# 	one_receipt = ask_api('invoice-receipts.get', {
	# 		'invoice-receipt-id' : result['id'] 	
	# 		})

	# 	self.assertEqual(one_receipt['permalink'], result['permalink'])
	# 	print 'Getted: ', one_receipt['permalink']


	# 	res = ask_api('invoice-receipts.update', {
	# 		'invoice-receipt-id': one_receipt['id'],
	# 		'due_date': one_receipt['due_date'],
	# 		'date': one_receipt['date'],
	# 		'client' : {
	# 			'name' : 'Ricardo Ferrera',
	# 			'code' : '122'
	# 		},
	# 		'items' : one_receipt['items']
	# 	})
	# 	print res

	def test_pdf_email(self):
		# list all and print 

		result = ask_api('invoice-receipts.list', {
			'per_page': 7,
			'page' : 1
			})

		print "Current page:" , result['current_page']
		for r in result['invoice_receipt']:
			print (
				'Id: {} Client: {}'.format (r['id'],r['client']['name']) 
			)

		
		a,b = result['invoice_receipt'][0], result['invoice_receipt'][1]


		# make finalize
		with self.assertRaises(errors.ApiCallError):
			result = ask_api('invoice-receipts.change-state', {
				'invoice-receipt-id': a['id'],
				'state': 'cancelled',
			})

		with self.assertRaises(errors.ApiCallError):
			result = ask_api('invoice-receipts.email-document', {
					'invoice-receipt-id': b['id'],

					'client': {
						'email': '???',
						'save': 0,
					},

					'subject' : 'The Html Letter',
					'body' : 'This <b>is Plain</b> text'
				})

		result = ask_api('invoice-receipts.related_documents', {
			'invoice-receipt-id' : a['id']

		})
		print result

		result = ask






if __name__ == '__main__':

	suite = unittest.TestLoader().loadTestsFromTestCase(InvoiceReceiptsApi)
	unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()