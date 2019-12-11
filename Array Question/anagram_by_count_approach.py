def func(a,b):
	a = a.replace(' ', '').lower()
	b = b.replace(' ', '').lower()
	count = {}
	if len(a) != len(b):
		return False
	else:
		for e in a:
			if e in count:
				count[e] += 1
			else:
				count[e] = 1
			
		for k in b:
			if k in count:
				count[k] -= 1
			else:
				return False
		
		for l in count:
			
			if count[l] != 0:
				return False
			else:
				return True						
					
print(func("abcc","abcd"))