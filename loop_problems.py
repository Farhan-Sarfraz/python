
# numbers = [1,-3,-4,-5,7,9,-6,44,-2,-56]

# positive_count = 0
# for num in numbers:
#     if num > 0:
#         positive_count += 1
# print(positive_count)

# n = int(input("Enter the number you want : "))

# sum_even = 0
# sum_odd = 0

# for num in range(1 , n + 1):
#     if(num % 2 == 0):
#         sum_even += num
# for i in range(1 , n + 1):
#     if( i % 2 != 0):
#         sum_odd += i

# print(sum_even)
# print(sum_odd)

# n = int(input("enter the number you want : "))

# for i in range(1,11):
#     if( i == 5):
#         continue
#     print(n , '*' , i , '=' , n * i)


# str = str(input("enter the number you want : "))

# # rev_str = ""

# # for i in str:
# #     rev_str = i + rev_str

# # print(rev_str)
# reversed = str[:: -1]

# print(reversed)

# text = str(input("enter the string : "))

# char_count = {}

# for char in text:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1

# for char in text:
#     if  char_count[char] == 1:
#         print("First non_repeated charachter. ")
#         break
#     else:
#         print("there is no non_repeated char.")

# Find first non-repeated character in a string
# text = input("Enter a string: ")

# char_count = {}

# for char in text:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1

# # Find the first character with count 1
# for char in text:
#     if char_count[char] == 1:
#         print("First non-repeated character is:", char)
#         break
# else:
#     print("No non-repeated character found.")


# num = int(input("enter the num : "))

# fact = 1

# for f in range(1 , num+1):
#     fact *= f
# print(fact)

# num = int(input("enter the num b/w 1 AND 10 : "))

# if num <= 10 and num >= 1:
#     print("valid input")
# else:
#     print("invalid")

# num = int(input("enter the num : "))

# if num <= 1:
#     print("not a prime number.")

# else:
#     for n in range(2,num ):
#         if(num % n == 0):
#             print("not a prime number.,")
#             break
#     else:
#             print("prime number.")
    

# num = int(input("enter the number : "))

# if num <= 1:
#     print(" number is not prime. ")
# else:
#     for i in range(2,num):
#         if(num % i == 0):
#             print("it's not a prime number. ")
#             break
#     else:
#         print("it's prime number. ")

# items = ["banana","mango","orange","apple","banana"]

# unique_item = set()

# for item in items:
#     if item in  unique_item:
#         print("duplicate ",item)
#         break
#     unique_item.add(item)

# import time

# wait_time = 1 
# retries = 5    

# for attempt in range(1, retries + 1):
#     print(f"Attempt {attempt}: waiting for {wait_time} seconds...")
#     time.sleep(wait_time)  
#     wait_time *= 2         


# i = 1

# while i < 11:
#     print(i)
#     i += 1

# sum = 0
# i = 1
# while i <= 50:
#     if i % 2 == 0:
#          sum = sum + i
#     i += 1

# print(sum)


