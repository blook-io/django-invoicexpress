import unittest


import uuid
from services import  ask_api

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
	def test_crud(self):
		result = ask_api('invoice-receipts.create', { 
				'date': '01/01/2014',
				'due_date': '01/02/2014',
				'client' : {
					'name' : 'Ricardo Pereira',
					'code' : 100,
				},
				'items type="array" ' : {
					'item' : [
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
					
				}
		})
		print result
		

if __name__ == '__main__':

	suite = unittest.TestLoader().loadTestsFromTestCase(InvoiceReceiptsApi)
	unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()