
# stack = []

# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print(stack[-1])

# print(len(stack)==0)

# print(len(stack))

# # stack = []

# # # Push elements
# # stack.append(10)
# # stack.append(20)
# # stack.append(30)

# # # Pop elements
# # print(stack.pop())  # Output: 30 (last element added)
# # print(stack.pop())  # Output: 20

# # # Peek at the top element
# # print(stack[-1])  # Output: 10

# # # Check if stack is empty
# # print(len(stack) == 0)  # Output: False

# # # Size of the stack
# # print(len(stack))  # Output: 1

# s = []

# s.append(11)
# s.append(22)

# print(s.pop())

# print(s[-1])

# print(len(s)==0)

# print(len(s))

# s = []

# s.append(3)
# s.append(2)

# print(s.pop())
# # print(s.pop())   we can't use s.pop for 2 for 2 input 
# #  
# print(s[-1])

# print(len(s)==0)

# print(len(s))


# class Stack:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.stack = [None] * capacity  
#         self.top = -1  
#     def push(self, item):
#         if self.is_full():
#             print("Stack overflow!")  
#             return
#         self.top += 1
#         self.stack[self.top] = item  
#     def pop(self):
#         if self.is_empty():
#             print("Stack underflow!") 
#             return None
#         item = self.stack[self.top]
#         self.stack[self.top] = None  
#         self.top -= 1
#         return item
#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.stack[self.top] 
#     def is_empty(self):
#         return self.top == -1  
#     def is_full(self):
#         return self.top == self.capacity - 1 
# stack = Stack(5)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())  
# print(stack.peek()) 
# print(stack.is_empty()) 
# print(stack.is_full())

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))