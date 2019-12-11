class Queue():
	"""
	making a queue with Double Stacks
	"""
	def __init__(self):
		self.instack = []
		self.outstack = []

	def enqueue(self, item):
		"""
		adds every new item to index[0] 
		"""
		self.instack.insert(0, item)

	def dequeue(self):
		while self.instack != []:
			# removing data from instack
			pop_data = self.instack.pop()
			
			# Adding poped data from instack to outstack with index on 0
			self.outstack.insert(0, pop_data)

		 # And Return ning Pop data 
		return self.outstack.pop()


s = Queue()	

for i in range(5):
	s.enqueue(i)
for j in range(5):
	print(s.dequeue())				