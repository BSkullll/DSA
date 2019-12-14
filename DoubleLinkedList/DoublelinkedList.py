class Node:
	"""
	Node for a Double Linked List 
	"""
	def __init__(self, data):
		"""
		A initializer when a object is created the below property is allocated in memeory for every
		objects.  
		"""
		self.data = data
		self.next = None
		self.prev = None


class DoubleLinkedList:
	"""
	This class will create a Double Linked list
	"""
	def __init__(self):
		self.head = None

	def print_list(self):
		"""
		This will print a DoubleLinkedlist
		"""	
		if self.head is None:
			print("list has no element")
			return 
		start = self.head
		while start != None:
			print(start.data, end=' ')
			start = start.next

	def insert_items_in_emptylist(self, data):
		if self.head is None:
			value = Node(data)
			self.head = value
			return 

		else:
			print("List is not empty")
			return 

	def prepend(self, data):
		"""
		Insert item at the start of the list 
		"""
		if self.head is not None:
			value = Node(data)
			value.next = self.head
			self.head.prev = value
			self.head = value
			return 
		else:
			insert_items_in_emptylist(data)

	def append(self, data):
		"""
		Insert item a the end of the list
		"""
		if self.head is None:
			value = Node(data)
			self.head = value
			return

		else:
			value = Node(data)
			start = self.head
			while start.next is not None:
				start = start.next
			else:
				start.next = value
				value.prev = start
				return

	def insert_item_after_another_item(self, item , data):
		"""
		This function will insert an item after some specific item
		"""
		if self.head is None:
			print("List is empty")
			return
		else:
			start = self.head
			while start is not None:
				if start.data  == item:
					break
				start = start.next
			if start == None:
				print("list has no ", item)
				return
			else:
				value = Node(data)
				value.next = start.next
				if start.next is not None:
					start.next.prev = value
				start.next = value
				value.prev = start
				# next_item = start.next
				# start.next = value
				# value.prev = start
				# value.next = next_item
				# next_item.prev = value
				# We Don't Need to store a next_item = start.next because start.next.prev = start hahah lol 
				return

	
	def insert_item_before_another_item(self, item, data):
		"""
		This will insert an item before some specific item 
		"""					
		if self.head is None:
			print("list is empty")
		else:
			start = self.head
			while start is not None:
				if start.data == item:
					break
				else:
					start = start.next
			if start is None:
				print(item, "is not in this list")
				return
			else:
				
				value = Node(data)
				
				value.next = start
				value.prev = start.prev
				if start.prev is not None:
					# print("Bye")
					start.prev.next = value
				else:	
					start.prev = value
					# print("hello")
					if self.head.data == item:
						self.head = value
					return

	def delete_element_start(self):
		"""
		This will delete an item of start
		"""
		if self.head is None:
			print("List has no elements")
			return
		else:
			start = self.head
			self.head = start.next
			if start.prev is not None:
				self.head.prev = None
			return 
			
	def delete_element_end(self):
		"""
		This will delete an last item 
		"""
		if self.head is None:
			print("List Has no element")
			return
		else:
			start = self.head
			while start.next is not None:
				start = start.next
			if start.prev is not None:	
				start.prev.next = None
			else:
				self.head = None

	def reverse(self):
		"""
		this will reverse a list
		"""
		##########
		# This is Linked List Opinion of reverese 
		# here we don't use the feature of double linked list
		# For reverse 
		# start = self.head
		# next = None
		# while start is not None:
		# 	q = start.next
		# 	start.next  = next
		# 	start.prev = q
		# 	next = start
		# 	start = q
		# else:	
		# 	self.head = next
		# 	print('hello')

		#############
		# Double Linked List Opinion
		# Done by another approach 
		if self.head is None:
			print("list is empty")
			return
		start = self.head
		p = start.next
		start.next =  None
		start.prev = p

		while p is not None:
			p.prev = p.next
			p.next = start
			start = p
			p = p.prev
		print()	
		self.head = start 		
	def delete_element_by_value(self, item):
		"""
		This will delete an specific element  
		"""
		if self.head is None:
			print("List has no element")
			return 

		if self.head.next == None:
			"""
			what if list has only one element  
			"""	
			
			if self.head.data == item:
				
				self.head = None
				return
			else:
				print(item," is not in list")
				return

		if self.head.next is not None:
			"""
			If the list has more item and the data is present in the first item of list
			"""
			if self.head.data == item:
				print("Hello")
				
				self.head = self.head.next
				self.head.prev = None
				return	

		start = self.head
		while start != None:
			if start.data == item: 		 					
				break
			else:
				start = start.next
		if start == None:
			print("list has no ", item)
		else:
			if start.next is None:
				start.prev.next = None

			else:
				
				start.next.prev =  start.prev
				start.prev.next = start.next
				return				



				
					
						    








list = DoubleLinkedList()
# list.head = Node(8)
# second = Node(6)
# third = Node(7)

# list.head.next = second
# second.prev = list.head

# second.next = third
# third.prev = second
# list.insert_items_in_emptylist(9)
# list.insert_items_in_emptylist(10)
# list.prepend(90)
list.append(96)
list.append(98)
list.append(100)
# list.insert_item_after_another_item(7, 100)
# list.insert_item_before_another_item(96, 100)
# list.insert_before_item(96, 100)
# list.delete_element_start()
# list.delete_element_end()
# list.delete_element_by_value(200)
list.print_list()
list.reverse()
list.print_list()


