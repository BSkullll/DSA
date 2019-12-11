class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):

		if self.head == None:
			print("Linked List has no element")
			return
		else:	
			start = self.head
			while start:
				print(start.data,end=' ')
				start = start.next


	def prepend(self, data):
		"""
		Add The Value at the first
		"""
		value = Node(data)
		value.next = self.head
		self.head = value

	def append(self, data):
		"""
		Add the value at the last
		"""	
		value = Node(data)
		if self.head == None:
			self.head = value
			return
		start = self.head
		while start.next != None:
			start = start.next
		else:	
			start.next = value	

	def insert_item_after_item(self, item, data):
		"""
		it's add an item after some specific item
		also it search wheter a item is present or not.

		"""
		value = Node(data)
		start = self.head
		while start != None:
			if start.data == item:
				break
			start = start.next

		if start == None:
			print(item, "is not in this list")
		else:
			value.next = start.next
			start.next = value
			return 		
			# value.next = start.next
			# start.next = value

	def insert_item_before_item(self, item, data):
		"""
		This will add an item before an item if the item is present   
		"""		
		

		if item == self.head.data:
			value = Node(data)
			value.next = self.head
			self.head = value
			return 


		value = Node(data)
		start = self.head
		while start.next != None:
			if start.next.data == item:
				break
			start = start.next
		if start.next == None:
			print(item,"is not in this list")
		else:
			value.next = start.next
			start.next = value

	def insert_item_at_location(self, index, data):
		"""
		This will insert an item at specific location

		"""	
		if index == 1:
			value = Node(data)
			value.next = self.head
			self.head = value
		else:	
			i = 1
			start = self.head
			while i < index-1 and start != None:
				start = start.next
				i += 1
			if start == None:
				print("index Out of Bound")
			else:
				value = Node(data)
				value.next = start.next
				start.next = value	

	def heads(self):
		return print('\n',self.head.data,) if self.head is not None else print("list has no  element ", end='\n')

	def tail(self):
		if self.head is None:							
			print("List has no item ")
			return 
		start  = self.head
		while start.next != None:
			start = start.next
		else:
			print(start.data)
			return
	def pop_first(self):
		"""
		This will remove a first item in the list
		"""
		if self.head == None:
			print("list has no element")
			return 
		self.head = self.head.next	

	def pop_last(self):
		if self.head  == None:
			print("List has no element")
			return
		start = self.head
		while start.next.next != None:
			start = start.next
		else:
			start.next = None

	def count(self):
		"""
		This will return an Count of items in the list
		"""	
		if self.head == None:
			return 0
		count = 0
		start = self.head
		while start is not None:
			start = start.next
			count += 1
		return print('\n',count)				

	def remove(self, item):
		"""
		Remove some specific item
		"""		
		if self.head == None:
			print("No item in this list")
			return 

		if self.head.data == item:
			self.head = self.head.next
			return

		start = self.head
		while start.next != None:
			if start.next.data == item:
				break 
			start = start.next
		if start.next == None:
			print(item, "is not present in this list")
		else:
			start.next = start.next.next

	def search(self, item):
		"""
		This will search an item and retrun true or False  
		"""					 	
		if self.head == None:
			return print("No item in this list ")
		start = self.head
		while start is not None:
			if start.data == item:
				print("item Found")
				return print(True)
			start = start.next
		
		print("not Found")
		return print(False)

	def reverse_list(self):
		"""
		This will reverse a list  
		"""
		prev = None
		start = self.head
		while start is not None:
			next = start.next
			start.next = prev
			prev = start
			start = next
		self.head = prev	


list = LinkedList()
list.head = Node(1)
second = Node(2)
third = Node(3)

list.head.next = second
second.next = third
# list.insert_item_at_location(4,600)
# list.pop_last()
# list.remove(2)
list.reverse_list()
list.print_list()
# list.count()
# list.search(9)
# list.pop_first()
# list.tail()
# list.print_list()


