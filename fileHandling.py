 
# # f = open("demo.txt","r")
# # data=f.read()
# # print(data)
# # print(type(data))

# # f.close

# f=open("demo.txt","r")
# sata=f.read(15)
# print(sata)

# f=open("demo.txt","r")
# sata=f.readline()
# print(sata)

# f = open("demo.txt","r")

# data = f.read()

# print(data)

# print(type(data))

# f.close()

# f = open("demo.txt","r")

# data = f.readline()

# print(data)

# data1 = f.readline()

# print(data1)

# f.close()

# f = open("demo.txt","r")

# data = f.read()

# print(data)

# line1 = f.readline()

# print(line1)

# line2 = f.readline()

# print(line2)

# f = open("demo.txt","w")

# data= f.write("i want to learn c. what is this.")

# print(data)

# f.close()

# f = open("demo.txt","a")

# data= f.write("\nthen i will move to java.")

# print(data)

# f.close()

# with open("demo.txt","r") as f:
    
#     data =f.read()

#     print(data)

# with open("demo.txt","w") as f:

#     data = f.write("new data enter")

#     print(data)

# with open("practice.txt","w") as f:

#     f.write("Hi everyone\nwe are learning file I/O\n")
    
#     f.write("using java.\nI like java")

# with open("practice.txt","r") as f:

#     data = f.read()

# newData= data.replace("java","python")

# print(newData)

# with open("practice.txt","r") as f:

#     data = f.read()

# newData= data.replace("java","python")

# print(newData)

# with open("practice.txt","w") as f:
 

#  f.write(newData)


# with open("practice.txt","w") as f:
#     f.write("hi evryone\nwe are learning file i/o java\nusing java.\ni like java.")

# with open("practice.txt","r") as f:

#     data = f.read()

# new_data=data.replace("java","python")

# print(new_data)

# with open("practice.txt","w") as f:

#     f.write(new_data)
    
# word = "python"

# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("founded")
#     else:
#         print("not found")

# def check_word():
#     word = "python"

#     with open("practice.txt","r") as f:
#        data = f.read()
#        if(data.find(word) != -1):
#           print("founded")
#        else:
#           print("not found")
# check_word()


# def check_line():
#     word="learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data ):
#                 print(line_no)
#                 return
#             line_no += 1
#         return -1
# check_line()

# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num=""
#         else:
#             num += data[i]

# count = 0
# with open("practice.txt","r") as f:
#     data=f.read()
#     num = data.split(",")
#     for val in num:
#         if(int(val)%2 == 0):
#             count += 1
# print(count)
  
# count = 0

# with open("practice.txt","r") as f:
#     data = f.read()

#     nums = data.split(",")

#     for val in nums:
#         if(int(val)%2 == 0):
#             count += 1

# print(count)
