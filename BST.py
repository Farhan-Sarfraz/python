# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
    
# def insert(root,val):
#     if root is None:
#         return Node(val)
#     if val < root.data:
#         root.left = insert(root.left,val)
#     elif val > root.data:
#         root.right = insert(root.right,val)
#     return root

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data, end=" ")
#         inorder(root.right)

# if __name__ == "__main__":
#     root = None
#     values = [50, 30, 70, 20, 40, 60, 80]

#     for val in values:
#         root = insert(root, val)

#     print("Inorder Traversal of BST:")
#     inorder(root)

# def search(root,key):
#     if root is None or root.data ==key:
#         return root
#     if key < root.data:
#         return search(root.left,key)
#     return search(root.right,key)

# def delete(root, key):
#     if root is None:
#         return root
#     if key < root.data:
#         root.left = delete(root.left, key)
#     elif key > root.data:
#         root.right = delete(root.right, key)
#     else:
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
#         temp = minValueNode(root.right)
#         root.data = temp.data
#         root.right = delete(root.right, temp.data)
#     return root

# def minValueNode(node):
#     current = node
#     while current.left:
#         current = current.left
#     return current

# def find_min(root):
#     current = root
#     while current.left:
#         current = current.left
#     return current.data

# def max_find(root):
#     current = root
#     while current.right:
#         current = current.right
#     return current.data

# def tree_height(root):
#     if not root:
#         return 0
#     return 1 + max(tree_height(root.left)),tree_height(root.right)
    

# def mirror_tree(root):
#     if root:
#         root.left,root.right = root.right,root.left
#         mirror_tree(root.left)
#         mirror_tree(root.right
#                     )
# Check recursively if every node obeys BST rule.
# def is_bst(node, left=None, right=None):
#     if not node:
#         return True
#     if left and node.data <= left.data:
#         return False
#     if right and node.data >= right.data:
#         return False
#     return is_bst(node.left, left, node) and is_bst(node.right, node, right)


# class Node:

#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# def insert(root,data):
#     if root is None:
#         return Node(data)
#     if data < root.data:
#         root.left = insert(root.left,data)
#     else:
#         root.right=insert(root.right,data)
#         return root
    
# def find_min(root):
#     while root.left:
#         root = root.left
#     return root.data

# def find_max(root):
#     while root.right:
#         root = root.right
#     return root.data

# def height(root):
#     if root is None:
#         return -1
#     return 1+ max(height(root.left),height(root.right))

# def is_bst(root,min_val = float('-inf'),max_val=float('inf')):
#     if root is None:
#         return True
#     if not (min_val < root.data < max_val):
#         return False
#     return is_bst(root.left,min_val,root.data) and is_bst(root.right,root.data,max_val)

# def mirror(root):
#     if root is None:
#         return 
#     root.left,root.right=root.right,root.left
#     mirror(root.left)
#     mirror(root.right)

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data,end=" ")
#         inorder(root.right)

# root = None
# values = [65,23,78,53,12,74]
# for v in values:
#     root = insert(root,v)

# print("Minimum Element:",find_min(root))
# print("Maximum Element:",find_max(root))
# print("Height OF tree:",height(root))
# print("is tree BST:",is_bst(root))
# print("Inorder before mirror:")
# inorder(root)
# mirror(root)
# print("\nInorder after mirror:")
# inorder(root)


    
    