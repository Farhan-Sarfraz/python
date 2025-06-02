# class Queue:
#     def __init__(self):
#         self.queue=[]
    
#     def enqueue(self,item):
#         self.queue.append(item)
#         print(f"enqueued: {item}")
    
#     def dequeue(self):
#         if self.is_empty():
#             return "queue underflow"
#         return self.queue.pop(0)
    
#     def peek(self):
#         if self.is_empty():
#             return "queue underflow"
#         return self.queue[0]
    
#     def is_empty(self):
#         return len(self.queue) == 0
    
#     def display(self):
#         if self.is_empty():
#             print("queue is empty")
#         else:
#             print("queue (front to rea) :" , self.queue)
 
# # q = Queue()
# # q.enqueue(10)
# # q.enqueue(20)
# # q.enqueue(30)
# # q.display()

# # print("peek :-> first element :",q.peek())
# # print("dequeued :",q.dequeue())
# # q.display()



# from collections import deque

# class FastQueue:
#     def __init__(self):
#         self.queue = deque()

#     def enqueue(self, item):
#         self.queue.append(item)

#     def dequeue(self):
#         if not self.queue:
#             return "Queue Underflow"
#         return self.queue.popleft()

#     def peek(self):
#         if not self.queue:
#             return "Queue is empty"
#         return self.queue[0]

#     def display(self):
#         print("Queue (front to rear):", list(self.queue))

# # ----------- Usage -----------
# fq = FastQueue()
# fq.enqueue('A')
# fq.enqueue('B')
# fq.enqueue('C')
# fq.display()
# print("Front:", fq.peek())
# print("Dequeued:", fq.dequeue())
# fq.display()


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedListQueue:
#     def __init__(self):
#         self.front = self.rear = None

#     def enqueue(self, data):
#         new_node = Node(data)
#         if self.rear is None:  # Queue is empty
#             self.front = self.rear = new_node
#             return
#         self.rear.next = new_node
#         self.rear = new_node

#     def dequeue(self):
#         if self.front is None:
#             return "Queue Underflow"
#         result = self.front.data
#         self.front = self.front.next
#         if self.front is None:  # Queue became empty
#             self.rear = None
#         return result

#     def peek(self):
#         if self.front is None:
#             return "Queue is empty"
#         return self.front.data

#     def display(self):
#         temp = self.front
#         print("Queue (front to rear):", end=" ")
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

# # ----------- Usage -----------
# llq = LinkedListQueue()
# llq.enqueue(1)
# llq.enqueue(2)
# llq.enqueue(3)
# llq.display()
# print("Front:", llq.peek())
# print("Dequeued:", llq.dequeue())
# llq.display()
def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
    return stack[0]




Task Scheduler: Schedule CPU tasks based on incoming jobs using a queue.
