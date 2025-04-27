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

