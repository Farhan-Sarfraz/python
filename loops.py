
# games = ["football","hocky","criket",]

# index = 0
# while index<=len(games) :
#     print(games[index])

#     index += 1

# values = (1,4,9,16,25,36,49,64,81,100)
# x = 49
# i = 0
# while i < len(values):
#     if(values[i] == x ):
#         print("key present at inedx ", i )
#     i += 1

# list = [1,2,3,4,6,32,76,96,54,24,658]
# i =0
# while i<len(list):
#     print(list[i])
#     i += 1
# i = 1
# while i <= 10 :
#      print(39*i)
#      i += 1
# i=100
# while i>=1 :
#     print(i) 
#     i -= 1

# i=1
# while i<=10 :
#     print(9*i)
#     i +=1
# i = 100
# while i>=1 :
#     print(i)
#     i -= 1
    
   
# count = 1
# while  count < 4:
#     print("hi")
#     count += 1



# print("loop endded")

#  break statements 

# num = (11,22,33,44,555,66,767,87,34,23)
# x=22
# i=0
# while i < len(num):
#    if( num[i] == x ):
#      print("found at index :", i)
#      break
#    else:
#     print("finding.....")

#     i += 1

# i = 0
# while i<=5 :
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i=i+1

# i = 0
# while i<=10 :
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i=i+1

# for loops 

# val=[1,2,3,4,5,6,7,8,9]
# val={"pak","ind","aus","afg"}

# for num in val:
#     print(num)

# nums={1,2,3,54,6,68,}

# for num in nums:
#     print(num)

# num = [1,4,9,16,25,36,49,64,81,100]

# for nums in num:
#     print(nums)

# num = (1,4,9,16,25,36,49,64,81,100)

# x = 16
# idx=0
# for nums in num:
#     if(nums==x):
#         print("number is found at idx:",idx)
#     idx += 1
     

#  range()

# print(range(5))

# seq = range(5)

# for i in seq:
#     print(i)

# for i in range(5): 
#     print(i)
# for i in range(1,5): 
#     print(i)
# for i in range(2,10,2): 
#     print(i)
# for i in range(100,0,-1): 
#     print(i)

# n = 10
# sum=0
# for i in range(1,n+1):
#     # print(i)
#     sum+=i
#     print(sum)

# n = 5
# fact = 1 
# i = 1 
# while i <= n :
#     fact *= i
#     i += 1

#     print(" fac of num  is  :", fact )

# students_height = input("enter the height of the students(seprated by the spaces). ")

# heights = students_height.split()

# for i in range(len(heights)):
#     heights[i] = int(heights[i])

# sumof_heights = 0
# for h in heights:
#     sumof_heights += h
# total_students = 0
# for s in heights:
#     total_students += 1
# avg_height = (sumof_heights/total_students)

# print(avg_height)

# students_marks = input("enter the number(seprated by spaces) of studensts.")
# student_nums = students_marks.split()
# for i in range(len(student_nums)):
#     student_nums[i] = int(student_nums[i])
# highest = student_nums[0]
# for n in student_nums:
#     if n > highest:
#         highest = n
# print(f"my highest score is: {highest}")
# number = 0
# for n in range(1,101):
#     number += n

# print(number)

# sum = 0

# for n in range(1, 101 ):
#     if n % 2 == 0:
#         sum += n

# print(sum)
# sum1 = 0
# for n in range(1, 101 ):
#     if n % 2 != 0:
#         sum1 += n
# print(sum1)
    
# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("fizzbuzz")
#     elif n % 3 == 0:
#         print("fizz")
#     elif n % 5 == 0:
#         print("buzz")
#     else:
#         print(n)

value = int(input("enter the number. "))
for n in range(1, 11):
    print(str(value) + " x " + str(n) +  " = "  + str(value * n))