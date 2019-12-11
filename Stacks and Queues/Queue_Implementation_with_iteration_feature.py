class Queue():
	"""
	Creating Queue with Features like FIFO(First in First Out) with iteration Feature
	which we can iterate on Onject by making an object iterable with iterator.
	"""
	def __init__(self):
		self.items = []
		self.index = 0

	# using iterator Protocol to make iterable Stack , that we can iterate upon.

	def __iter__(self):
		"""
		making an object iterable
		"""
		return self  

	def __next__(self):
		"""
		This is also a protocol function for traversing next item 
		"""
		try:

			current = self.items[self.index]
			self.index += 1
			return current
		except:
			raise StopIteration()		

	def enqueue(self, item):
		"""
		Adds a new item to the rear of the queue.
		"""	
		self.items.insert(0, item)

	def dequeue(self):
		"""
		Removes the Front item from the queue.
		"""
		self.items.pop()

	def isEmpty(self):
		"""
		tests to see whether the queue is empty.
		"""	
		return self.items == []

	def size(self):
		"""
		Returns the number of items in the queue.
		"""	
		return len(self.items)


s = Queue()

s.enqueue("First")
s.enqueue("Second")

s.dequeue()
for e in s:
	print(e)	