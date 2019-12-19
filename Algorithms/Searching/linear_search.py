def linear_search(data, key):
	"""
	For an  unoredered list
	"""
	count = 0
	while count < len(data):
		if data[count] == key:
			return print('result found at index', count)

		count += 1
	else:
		return print("result Not Found")	

def unordered_linear_saerch(data, key):
	"""
	For ordered list
	"""
	count = 0
	stop = False
	while count < len(data) and not stop:
		if data[count] == key:
			return print('Result Found at Index', count)

		if data[count] > key:
			stop = True
			return print('Result Not Fund')
		else:
			count += 1



unordered_linear_saerch([1,2,3,5,8],7)		


