# n=20
# if(n>=222):
#     print(" number is greater :")
# elif(n<=2):
#     print(" number is lesser :")

# num=100

# if(num>33):
#     print("pass :")
# elif(num<33):
#     print(" fail :")
# else:
#     print(" no result :")

# num=int(input("enter the marks :"))

# if(num>=90):
#     grade="A"
# elif(num<90 and num>=80):
#      grade="B"
# elif(80<num and num>=70):
#      grade="C"
# else:
#      grade="D"
# print("garde of the students :", grade)

#  nesting

# age = 22

# if(age>18):
#     if(age>60):
#         print("will die.")

#     print("can drive.")

# else:

#     print("both can't.")

# num = int(input("Enter the num."))
# if(num%2 == 0):
#     print(" number is even.")
# elif(num%2!= 0):
#     print(" number is odd.")

# n1=int(input("enter first num."))
# n2=int(input("enter second num."))
# n3=int(input("enter third num."))

# if(n1>n2 and n1>n3):
#     print(" n1 is greatest of three number.")
# elif(n2>n1 and n2>n3):
#     print(" n2 is greatest of three number.")
# else:
#     print(" n3 is greatest of three number.")

# n =int(input("enter  num."))
# if(n%7 == 0):
#     print("yes it is multiple.")
# else:
#     print("it is not.")


# num = int(input("enter the num: "))

# if num % 2 == 0:
#     print("even number it is.")
# else:
#     print("odd number.")

# height = int(input("enter height : "))
# age = int(input("enter age :"))

# if height >= 120:
#     print("you are allowed to ride.")
#     if age > 18:
#         print("ticket price is 10$.")
#     else:
#         print('ticket price is 5$')
# else:
#     print("you are't allowed to ride.")

# weight = float(input("enter your weight :"))
# height = float(input("enter your height :"))

# bmi = round(weight/height**2)
# if bmi < 18.5:
#     print(f"you are bmi is {bmi} , you are  underweight.")
# elif bmi < 25:
#     print(f"you are bmi is {bmi} , you are  nomalweight.")
# elif bmi < 30:
#     print(f"you are bmi is {bmi} , you are  overweight.")
# elif bmi < 35:
#     print(f"you are bmi is {bmi} , you are obese.")
# else:
#     print(f"you are bmi is {bmi} , you'r clinically obese.")



# year = int(input("enter the year do you want to check :"))

# if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
#     print("it's a leap year. ")
# else:
#     print("it's not a leap year. ")
    
name1 = input("what is  your name.").lower()
name2 = input("what's their  name.").lower()

comb_name = name1 + name2

t = comb_name.count("t")
r = comb_name.count("r")
u = comb_name.count("u")
e = comb_name.count("e")

l = comb_name.count("l")
o = comb_name.count("o")
v = comb_name.count("v")
e2 = comb_name.count("e")

true = t + r + u + e
love = l + o + v + e2

score = int(str(true) + str(love))
print(f"\nYour love score is: {score}%")

if score > 80:
    print("You are a perfect match! ")
elif score > 50:
    print("You both have a good connection. ")
else:
    print("You might need to work on your relationship.")