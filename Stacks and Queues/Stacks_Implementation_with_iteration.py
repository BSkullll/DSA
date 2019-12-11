class Stack():
	"""
	Creating Stacks with features like LIFO (Last In First Out)  
	"""
	def __init__(self):
		self.items = []
		self.value = 0

	def is_empty(self):
		"""
		Checking a stack is empty or not 
		"""
		return self.items == []

	def push(self, item):
		"""
		Pushing items to the stacks 
		"""	
		self.items.append(item)

	def pop(self):
		"""
		Poping items From the Stack in LIFO Manner 
		"""	
		self.items.pop()

	def length(self):
		"""
		Checking length of Stack 
		"""	
		return len(self.items)

	def peek(self):
		"""
		Rerturning the Top item Form the Stack 
		"""	
		return self.items[-1]

	# making an Iterator that makes an object iterable

	def __iter__(self):
		return self 

	def __next__(self):
		try:
			current = self.items[self.value]
			self.value += 1
			return current
		except:
			raise StopIteration()		


s = Stack()
s.push("Hello")
for e in s:
	print(e)
