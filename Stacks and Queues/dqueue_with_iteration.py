class Dequeue():
	"""
	Creating a Dequeue with Hybrid Feature Like adding and poping from both side.
	"""
	def __init__(self):
		self.items = []
		self.value = 0

	def __iter__(self):
		"""
		This is used to make an iterator
		"""
		return self

	def __next__(self):
		"""
		This is also used to make an iterator 
		"""
		try:
			current = self.items[self.value]
			self.value += 1
			return current
		except:
			raise StopIteration()	


	def addFront(self, item):
		"""
		Adding data to the last or Front
		"""
		self.items.append(item)

	def addRear(self, item):
		"""
		Adding data to the rear or First mean left first
		"""
		self.items.insert(0, item)	

	def removeFront(self):
		"""
		Removing the Front data and return those data 
		"""	
		return self.items.pop()

	def removeRear(self):
		"""
		Remove the data From the rear  
		"""	
		return self.items.pop(0)

	def isEmpty(self):
		"""
		Checking the Dequeue is empty or not
		"""	
		return self.items == []

	def size(self):
		"""
		Return the length of Dequeue
		"""
		return	len(self.items)

	
d = Dequeue()

d.addFront("1")
d.addRear("2")

for e in d:
	print(e)		
	






