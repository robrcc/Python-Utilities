from checknumbers import *

# Converts all numeric text in a list to ints and floats
def convert_list_numbers( myList ):
	for x in range(len(myList)):
		val = myList[x]
		if isInt(val):
			val = int(val)
			myList[x] = val
		elif isFloat(val):
			val = float(val)
			myList[x] = val
			


# Example CSV string received from Arduino
reading = "-12.7,23.3,18.3,3432.232,A,Awake\n"

# Split string into list of six (text) values
values_str = reading.strip().split(",")
print(values_str)

# Convert all numeric text to int/float data
convert_list_numbers(values_str)
print(values_str)

