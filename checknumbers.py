def isInt( userInput ):
	try:
		val = int(userInput)
		return True
	except ValueError:
		return False

def isFloat( userInput ):
	if isInt(userInput): return False
	try:
		val = float(userInput) 
		return True
	except ValueError:
		return False
			
def isNumber( userInput ):
	if isFloat(userInput) or isInt(userInput):
		return True
	return False

