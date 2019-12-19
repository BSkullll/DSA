def func(a, key):

	first = 0
	last  = len(a)-1
	found = False
	while first <= last and not found:
		mid = first + last // 2
		if a[mid] == key:
			found = True
		else:
			if key < a[mid]:
				last = mid-1
				print(last)
			else:
				first = mid+1 
				print(first)
	return found			

				
		


				
print(func([0,1,2,3], 3))
					
