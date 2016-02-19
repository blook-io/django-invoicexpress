# 

# error during call
class ApiCallError(Exception):
	pass

# error when feature 
class ApiUndocumented(Exception):
	pass

class WrongParams(Exception):
	pass