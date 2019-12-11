def func(a, b):
	
		
	for e in a:
		for j in range(1, len(a)):
			if e+a[j] == b:
				print((e,a[j]))
				a.remove(e)
				
				break
	
	
func([1,3,2,2],4)		
