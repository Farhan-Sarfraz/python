

# q1

# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("it's done. ")
# my_function()

# solution 

# def my_function():
#     #  bcz range function works from 0 ,1,2,3,4,5 etc so instead of 1 to 20 we should considered 1 to 21
#     for i in range(1, 21):
#         if i == 20:
#             print("it's done. ")
# my_function()

# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("That's not a number!")


#  wrong

# from random import randint
# rand_nums = ["1" , "2", "3", "4", "5"]
# dice_num = randint(1, 5)
# print(rand_nums[dice_num])

#  correct

# from random import randint
# rand_nums = ["1" , "2", "3", "4", "5"]
# dice_num = randint(0, 4)
# print(rand_nums[dice_num])


# problem

# year = int(input("enter the year. "))

# if year > 1980 and year < 1994:
#     print("you were millenial. ")
# elif year > 1994:
#     print("you are gen z. ")

# soltuion

# year = int(input("enter the year. "))

# if year > 1980 and year <= 1994:
#     print("you were millenial. ")
# elif year > 1994:
#     print("you are gen z. ")
 
 
# pages = 0
# word_per_pages = 0

# pages = int(input("enter the pages. "))
# word_per_pages = int(input("enter the word per page. "))

# total_words = pages * word_per_pages

# print(f"pages = {pages}")
# print(f"word_per_pages = {word_per_pages}")

# print( total_words)


#  problem

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_list = item * 2
#     b_list.append(new_list)
#     print(b_list)
# mutate([1,2,3,5,8,13])

#  solution
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_list = item * 2
#         b_list.append(new_list)
#     print(b_list)
# mutate([1,2,3,5,8,13])

# num = int(input("enter the number. "))

# if num % 2 == 0:
#     print("it's even number. ")
# else:
#     print("it's odd number. ")

year = int(input("enter the year. "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("it's leap year. ")
else:
    print("it's not a leap year. ")