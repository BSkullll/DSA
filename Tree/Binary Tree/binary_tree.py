class BinaryTree:
	def __init__(self, root):
		self.key = root
		self.left = None
		self.right = None

	def insert_left(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.left = self.left
			self.left = t

	def insert_right(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.right = self.right
			self.right = t

	def get_right_child(self):
		return self.right

	def get_left_child(self):
		return self.left
	
	def setRoot(self, root):
		self.key = root

	def getRoot(self):
		return self.key

	# def post_order_traverse(self):
	# 	if self.left:
	# 		self.left.post_order_traverse()
	# 	if self.right:
	# 		self.right.post_order_traverse()
	# 	print(self.key, end=' ')
		# Beow function is same as this method

def insert(root, data):
	q = []
	q.append(root)
	while True:
		temp = q[0]
		q.pop(0)
		a = True
		
		if temp.left == None:
			temp.left = BinaryTree(data)
			break
		else:
			q.append(temp.left)

		if temp.right == None:
			temp.right = BinaryTree(data)
			break
		else:
			q.append(temp.right)			

def delete_deepest_node(root, node):
	q = []
	q.append(root)
	while len(q):
		temp = q.pop(0)
		
		if temp.right is node:
			temp.right = node
			return
		else:
			q.append(temp.right)

		if temp.left is node:
			temp.left = None
			return
		else:
			q.append(temp.left)				





def post_order_traverse(tree):
	if tree:
		
		post_order_traverse(tree.get_left_child())
		
		post_order_traverse(tree.get_right_child())
		print(tree.getRoot(), end= ' ')
		
	elif tree == None:
		return

def preTraverse(tree):
	if tree:
		print(tree.getRoot(), end= ' ')
		preTraverse(tree.get_left_child())
		
		preTraverse(tree.get_right_child())
		
	elif tree == None:
		return

def inorder_Traverse(tree):
	if tree:
		inorder_Traverse(tree.left)
		print(tree.key)
		inorder_Traverse(tree.right)
	else:
		return

def level_order_traversal(root):

	if root == None:
		return

	q = []
	# data = []
	q.append(root)

	while len(q)>0:
		temp = q[0]
		print(temp.key, end=' ')
		q.pop(0)
		if temp.left is not None:
			q.append(temp.left)

		if temp.right is not None:
			q.append(temp.right)

def level_order_traversal_reversal(root):
	q = []
	data = []			
	q.append(root)

	while len(q)>0:
		temp = q[0]
		# print(temp.key, end=' ')
		data.append(temp.key)
		q.pop(0)

		if temp.left is not None:
			q.append(temp.left)

		if temp.right is not None:
			q.append(temp.right)

	print()		
	while len(data)>0:
		temp = data.pop()

		print(temp, end= ' ')		
def deleteDeepest(root,d_node): 
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 

        if temp.key is d_node: 

            temp = None
            
            return
        if temp.right: 
            if temp.right is d_node: 
                temp.right = None
                return
            else: 
                q.append(temp.right) 
        if temp.left: 
            if temp.left is d_node: 
                temp.left = None
                return
            else: 
                q.append(temp.left) 
   
# function to delete element in binary tree  
def deletion(root, key): 
    if root == None : 
        return None
    if root.left == None and root.right == None: 
        if root.key == key :  
            return None
        else : 
            return root 
    key_node = None
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp.key == key: 
            key_node = temp 
        if temp.left: 
            q.append(temp.left) 
        if temp.right: 
            q.append(temp.right) 
    if key_node :  
        x = temp.key 
        deleteDeepest(root,temp) 
        key_node.key = x 
    return root 


	



r = BinaryTree('A')

r.left = BinaryTree('B')
r.right = BinaryTree('C')

r.left.left = BinaryTree('D')
r.left.right = BinaryTree('E')

r.right.left = BinaryTree('F')
r.right.right = BinaryTree('G')

# delete_binary_tree(r)
# level_order_traversal(r)
# # level_order_traversal_reversal(r)
# post_order_traverse(r)
# delete_deepest_node(r,'Hello')
k = deletion(r,'G')
level_order_traversal(r)