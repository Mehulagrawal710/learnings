#The function works for any level of nested dictionary
def traverseNestedDict(d):
    stack = list(d.items())
    while stack:
        k, v = stack.pop()
        if isinstance(v, dict):
            stack.extend(v.items())
        else:
        	print(k, v)

d = {
	'k1': 5,
	'k2': {
		'ik1':{
			'iik1':6,
			'iik2':7
		},
		'ik2':2
	}
}

traverseNestedDict(d)