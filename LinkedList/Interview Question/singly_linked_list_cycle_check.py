class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Linked_list:
	def __init__(self):
		self.head = None

	def traverse(self):
		start = self.head
		while start is not None:
			print(start.data)
			start = start.next

def check_cycle(Node):
	check = Node
	start = Node
	while start is not None:
		start = start.next
		if start is None:
			return False
		elif start.next == check:
			return True			

def check_nth_last_node(nth, startign_Node):
	total = 1
	count = 1
	start = startign_Node
	while start is not None:
		total += 1
		start = start.next

	check = total - nth

	# new = startign_Node
	helo = startign_Node
	while check != count:
		# new = new.next
		
		count += 1
		helo = helo.next
	else:
		print("nth Node Data",helo.data)	

	
list = Linked_list()
list.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5) 				


list.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# print(check_cycle(list.head))
list.traverse()
check_nth_last_node(3, list.head)


