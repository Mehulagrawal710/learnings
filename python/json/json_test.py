import json

with open('test.json') as jsonfile:
	data = json.load(jsonfile)
	print(data)

data = {
	'firstname': 'Mehul',
	'lastname':'Agrawal'
}

with open('write.json', 'w') as outfile:
	json.dump(data, outfile, indent=4)

"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python		JSON
dict		Object
list		Array
tuple		Array
str			String
int			Number
float		Number
True		true
False		false
None		null
"""