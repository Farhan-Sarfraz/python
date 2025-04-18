# class Node:
#     def __init__(self, data):
#         self.data = data     
#         self.next = None      

# class LinkedList:
#     def __init__(self):
#         self.head = None      
#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return
        
#         last = self.head
#         while last.next:
#             last = last.next
        
#         last.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# ll = LinkedList()
# ll.append(10)
# ll.append(20)
# ll.append(30)

# ll.display()

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linked:
#     def __init__(self):
#         self.head=None
    
#     def append(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#             return
#         last=self.head
#         while last.next:
#             last=last.next
        
#         last.next=new_node
#     def display(self):
#         current =self.head
#         while current:
#             print(current.data)
#             current = current.next
#         print("none")

# ll=linked()
# ll.append(10)
# ll.append(20)

# ll.display()

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=' -> ')
#             temp = temp.next
#         print('None')

# # Example
# ll = SinglyLinkedList()
# ll.insert_at_beginning(30)
# ll.insert_at_beginning(20)
# ll.insert_at_beginning(10)
# ll.display()  # Output: 10 -> 20 -> 30 -> None



# class DNode:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = DNode(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node
#         new_node.prev = temp

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=' <-> ')
#             temp = temp.next
#         print('None')

# # Example
# dll = DoublyLinkedList()
# dll.append(10)
# dll.append(20)
# dll.append(30)
# dll.display()  # Output: 10 <-> 20 <-> 30 <-> None


