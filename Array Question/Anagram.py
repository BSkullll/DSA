def func(a, b):

	a = a.replace(' ','').lower()
	b = b.replace(' ','').lower()
	result = None
	result2 = None
	if len(a) != len(b):
		return False

	else:
		for e in a:
			if e in b:
				result = True
				continue
			else:
				result = False
				break
		for j in b:
			if j in a:
				result2 = True
			else:
				result2 = False
				break
		if result and result2:
			return True
		else:
			return False				

print(func('abcc','abcd'))