def func(a, b):
	a = a.replace(' ', '').lower()
	b = b.replace(' ', '').lower()
	result = None
	
	if len(a) != len(b):
		return False
	else:
		a = sorted(a)
		b = sorted(b)

		for i in range(len(a)):
			if a[i] == b[i]:
				result = True
				continue
			else:
				result = False
				break
	return result

print(func("abcc","abcd"))						
			