# Define variables
# name = "Ali"
# age = 25
# is_student = True
# # Print variables
# print("Name:", name)
# print("Age:", age)
# print("Is Student:", is_student)

# integer_value = 10
# float_value = 20.5
# string_value = "Hello Python"
# boolean_value = True
# # Print data types
# print(type(integer_value))
# print(type(float_value))
# print(type(string_value))
# print(type(boolean_value))

# num = 10
# decimal = 5.7
# text = "123"
# # Arithmetic operations
# print("Sum:", num + decimal)
# print("Product:", num * decimal)


# text = "Python Programming"

# # Slicing
# print("First 6 characters:", text[:6])
# print("Last 6 characters:", text[-6:])

# # Concatenation
# greeting = "Hello, "
# print("Greeting:", greeting + text)

# # String methods
# print("Uppercase:", text.upper())
# print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

# Boolean values
# a = 10
# b = 20
# print("Is a equal to b?", a == b)
# print("Is a less than b?", a < b)
# print("Logical AND:", a < b and b > 15)
# print("Logical OR:", a > b or b > 15)



# x = 15
# y = 4
# # Arithmetic operators
# print("Addition:", x + y)
# print("Division:", x / y)
# # Comparison operators
# print("Is x greater than y?", x > y)
# # Logical operators
# print("Logical AND:", x > 10 and y < 5)

# fruits = ["apple", "banana", "cherry"]
# # Accessing list items
# print("First fruit:", fruits[0])
# # Modifying list
# fruits.append("orange")
# print("List after adding orange:", fruits)
# # Looping through list
# for fruit in fruits:
#     print("Fruit:", fruit)

 # Tuples

# colors = ("red", "green", "blue")
# print("First color:", colors[0])
# # Unpacking tuple
# (a, b, c) = colors
# print("Unpacked values:", a, b, c)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# # Input from user
# num = int(input("Enter a number: "))
# print("Factorial of", num, "is", factorial(num))


# number = int(input("Enter a number: "))

# # Check if the number is positive, negative, or zero
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")


# Dictionaries
# student = {"name": "Alice", "age": 21, "grade": "A"}
# student["age"] = 22
# print("Updated dictionary:", student)
# # Loop through dictionary
# for key, value in student.items():
#     print(key, ":", value)

grades=[]

for i in range(5):
    grade=float(input(f"enter the course num{i+1} "))
    grades.append(grade)
    gpa=sum(grades)/len(grades)
    print("gpa is :",gpa)