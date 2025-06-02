
# dic={

#     "key" : "value",
#     "Name" : "ali",
#     "rollnum" : 21,
#     "marks" : 99.3,
#     "subj" : ["ss","eng","urdu"],
#     77 : 88.6,
# }

# print(dic)
# print(type(dic))

# dic={

#     "key" : "value",
#     "Name" : "ali",
#     "rollnum" : 21,
#     "marks" : 99.3,
#     "subj" : ["ss","eng","urdu"],
#     77 : 88.6,
# }

# print(dic["Name"])

# print(dic["key"])

# student = {
#     " name " : " ali ",
#     " subjects "  : {
#         "chem"  :  842,
#         "bio"  : 785,
#         "math"  : 237,
#     }
# }
# print(student)
# print(student[" subjects "])
# print(student[" subjects "]["bio"])

# student = {
#     " name " : " ali ",
#     " subjects "  : {
#         "chem"  :  842,
#         "bio"  : 785,
#         "math"  : 237,
#     }
# }
# print(student.keys())
# print(len(student))

# print(list(student))

# student = {
#     " name " : " ali ",
#     " subjects "  : {
#         "chem"  :  842,
#         "bio"  : 785,
#         "math"  : 237,
#     }
# }
# print(student.items())
# print(len(student))

# print(list(student))

# student = {
#     " name " : " ali ",
#     " subjects "  : {
#         "chem"  :  842,
#         "bio"  : 785,
#         "math"  : 237,
#     }
# }
# print(student.get(" name "))


# student = {
#     " name " : " ali ",
#     " subjects "  : {
#         "chem"  :  842,
#         "bio"  : 785,
#         "math"  : 237,
#     }
# }
# print(student.update({"city":"muy"}))
# print(student)

# dict={
#     "cat"  : " a small animal",
#     "table" : ["a piece of the furniture", "list of the facts and figures"]
# }

# print(dict)

# dict={
#     "java","pyhton","java","c","javascripts",
#       "c++","c++","java",
# }

# print(dict)
# print(len(dict))

# marks={}
# x=int(input("enter the phy marks :"))
# marks.update({"phy :" : x})

# x=int(input("enter the che marks :"))
# marks.update({"che :":x})

# x=int(input("enter the bio marks :"))
# marks.update({"bio :":x})

# print(marks)

student = {
    "name" : "ali",
    "roll" : 9,
    "subj" : {
        "math" : 77,
        "eng" : 73,
    }
    
}

# print(student["subj"]["eng"])
# print(type(student))
print(student.values())