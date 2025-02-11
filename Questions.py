
# num=int(input("enter the number "))

# if(num > 0 ):
#     print("number is positive.")
# if(num == 0):
#     print("num is zero.")
# if(num<0):
#     print("number is -ve")


# a = 10

# b = 15

# sum = a+b

# print(sum)

# print(type(sum))

# a=int(input("enter the first val."))
# b=int(input("enter the second val."))
# c=int(input("enter the 3rd val."))

# if(a>b and b>c):
#     print("a is maxi")
# if(b>a and b>c):
#     print("b is maxi")
# if(c>a and c>b):
#     print("c is maxi")

# text = input("Enter a string: ")

# print("Reversed string:", text[::-1])

# str = input("enter the str :")

# updated=str[::-1]

# print("revese str is :",updated)

# n = int(input("enter the num"))

# if(n%2==0):
#     print("n is even.")
# else:
#     print("n is odd.")


# n = int(input("enter the num :"))

# for i  in range(0,10):
#     i += 1

#     val = i * n

#     print("multiplication table is . ", val  )


# n = int(input("enter the number :"))

# factorial = 1

# for i in range(1,n+1):

#     factorial *= i

#     print("Factorial of num is :",factorial)

# text = input("Enter a string: ")

# vowels = "aeiouAEIOU"

# count = sum(1 for char in text if char in vowels)

# print("Number of vowels:", count)

# t = input("String is :")

# vowels = "aeiou"

# count= sum(1 for chr in t if  chr in vowels)

# print("total vowels are : ",count)

# celsius = float(input("Enter temperature in Celsius: "))

# fahrenheit = (celsius * 9 / 5) + 32

# print("Temperature in Fahrenheit:", fahrenheit)


# units = int(input("Enter units consumed: "))

# Calculate bill based on tariff
# if units <= 100:
#     bill = units * 30  
# elif 101 <= units <= 300:
#     bill = 100 * 30 + (units - 100) * 40 
# else:
#     bill = 100 * 30 + 200 * 40 + (units - 300) * 60 

# # Add fixed charges
# bill += 1500  
# bill += 200   

# # Print the total bill
# print("Total bill:", bill)


# Input principal loan amount
# P = float(input("Enter principal loan amount: "))

# # Input annual interest rate and convert to monthly rate
# R = float(input("Enter annual interest rate (%): ")) / 12 / 100

# # Input number of monthly installments
# N = int(input("Enter number of monthly installments: "))

# # Calculate EMI using the formula
# EMI = (P * R * (1 + R) ** N) / ((1 + R) ** N - 1)

# # Print the EMI
# print("EMI:", EMI)

# Input monthly income
income = float(input("Enter monthly income: "))

# Input expenses for different categories
# rent = float(input("Enter rent: "))
# food = float(input("Enter food expenses: "))
# transport = float(input("Enter transportation expenses: "))
# savings = float(input("Enter savings: "))

# # Calculate remaining balance or deficit
# total_expenses = rent + food + transport + savings
# balance = income - total_expenses

# # Print the result
# if balance >= 0:
#     print("Remaining balance:", balance)
# else:
#     print("Deficit:", -balance)