# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []

#     def add_child(self, child):
#         self.children.append(child)

# def print_tree(node, level=0):
#     print(" " * level * 2 + node.data)
#     for child in node.children:
#         print_tree(child, level + 1)


# class Node:
    
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# def preorder_traversal(root):
#     if root:
#         print(root.data, end=" ")
#         preorder_traversal(root.left)
#         preorder_traversal(root.right)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def insert(root, key):
#     if root is None:
#         return Node(key)
#     if key < root.data:
#         root.left = insert(root.left, key)
#     else:
#         root.right = insert(root.right, key)
#     return root

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data, end=" ")
#         inorder(root.right)

# root = Node(10)
# insert(root, 5)
# insert(root, 15)
# insert(root, 2)

# inorder(root)

# class Node:
    
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# def insert_iterative(root, key):
#     new_node = Node(key)
#     if root is None:
#         return new_node

#     current = root
#     while True:
#         if key < current.data:
#             if current.left is None:
#                 current.left = new_node
#                 break
#             current = current.left
#         else:
#             if current.right is None:
#                 current.right = new_node
#                 break
#             current = current.right
#     return root

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data, end=" ")
#         inorder(root.right)

# root = Node(16)
# insert_iterative(root, 20)
# insert_iterative(root, 30)
# insert_iterative(root, 15)

# inorder(root)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# def insert(root , key):
#     if root is None:
#         return Node(key)
#     if key < root.data:
#         root.left = insert(root.left,key)
#     if key > root.data:
#         root.right = insert(root.right,key)
#     return root

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data, end=" ")
#         inorder(root.right)

# root = Node(35)
# insert(root,10)
# insert(root,20)
# insert(root,30)

# inorder(root)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.children = []
    
#     def add_child(self,child):
#         self.children.append(child)
    
#     def print_tree(node,level=0):
#         print(" " * level * 2 + node.data)
#         for child in node.children:
#             print_tree(child,level+1)

#     def inorder(node):
#         if node:
#             inorder(node.left)
#             print(node.data,end="")
#             inorder(node.right)
#     def bfs(root):
#         queue = deque([root])
#         while queue:
#             node=queue.popleft()
#             print(node.data,end=" ")
#             if node.left:
#                 queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# def in_order(root):
#         if root:
#             in_order(root.left)
#             print(root.data,end=" ")
#             in_order(root.right)

# def pre_order(root):
#      if root:
#           print(root.data,end=" ")
#           pre_order(root.left)
#           pre_order(root.right)

# def post_order(root):
#      if root:
#           post_order(root.left)
#           post_order(root.right)
#           print(root.data,end=" ")

# def level_order(root):
#      if root is None:
#           return
#      queue = [root]
#      while  queue:
#           node = queue.pop(0)
#           print(node.data,end=" ")

#           if node.left:queue.append(node.left) 
#           if node.right:queue.append(node.right)

# root = Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.right.left=Node(6)
# root.right.right=Node(7)

# print("In_order triversal is :",end=" ")
# in_order(root)
# print()

# print("Pre_order triversal is :",end=" ")
# pre_order(root)
# print()

# print("Post_order triversal is :",end=" ")
# post_order(root)
# print()
        
# print("level_order triversal is :",end=" ")
# level_order(root)
# print()




             