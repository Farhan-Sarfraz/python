
# class Student:
#     def __init__(self,full):
#         self.name=full
#         print(" creating the constructor.")

# s1=Student("ali")
# print(s1.name)


# class Student:
#     name=" ali "
#     def __init__(self):
#         print(" creating the constructor.")
#         name=" ali "

# s1=Student()
# print(s1.name)

# class Student:
#     def __init__(self,full):
#         self.name=full
#         print(" creating the constructor.")

# s1=Student("ali")
# print(s1.name)



# class Student:
#     name="ali"

# s1=Student()
# print(s1.name)

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#          sum=0
#          for val in self.marks:
#                 sum += val
#                 print("HI", self.name , "your avrage marks are ", sum/3 )
        
    
# s1=Student("Ali khan ", [90,80,70] )
# s1.get_avg()


# abstraction

# class Car:
#     def __init__(self):
#         self.accelerator=False
#         self.clutch=False
#         self.brk=False
#     def start(self):
#         self.accelerator=True
#         self.clutch=True
#         print("car is start.")
# c1=Car()
# c1.start()


class Account:
    def __init__(self,bal,accNo):
        self.balance=bal
        self.account=accNo

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited.")
        print("Total balance is = ", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("Total balance is = ", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=Account(100,123)
acc1.debit(20)
acc1.credit(1000)
