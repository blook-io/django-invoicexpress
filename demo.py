## need to run this script in console 
# as
# ./manage.py shell < django_invoicexpress/demo.py

from django_invoicexpress.services import ask_api

result = ask_api( 'user.accounts')

your_account = result['accounts']['account']
print """
Data of your account 
id : {id},
name : {name},
url : {url} 
""".format(**your_account)

