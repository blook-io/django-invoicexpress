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



# print """
# -----------------------
# Updating first user
# -----------------------
# """

# print """
# -------------------------
# Getting one (first) user
# -------------------------
# """



# # print "Updating user"
# # print "Removing user"


if __name__ == '__main__':
    unittest.main()