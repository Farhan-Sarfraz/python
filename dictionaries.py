
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

# student = {
#     "name" : "ali",
#     "roll" : 9,
#     "subj" : {
#         "math" : 77,
#         "eng" : 73,
#     }
    
# }

# print(student["subj"]["eng"])
# print(type(student))
# print(student.values())

# dictionaries = {
#     "bug" :  "error in program that prevents the program to run. ",
#     "function" : "piece of data that call over again and again. ",
#     "loop" : "action that have been performed repeadetly. ",
#     "new" : "something to happened soon. "
# }

# print(dictionaries.keys())
# print(dictionaries.values())
# print(dictionaries.items())
# print(dictionaries["loop"])
# print(dictionaries)
# dictionaries["new"] = "something is changed."
# print(dictionaries)
# dictionaries = {}
# print(dictionaries)

# for key in dictionaries:
#     print(key)
#     print(dictionaries[key])

# student__marks = {
#     "ali" : 93,
#     "usman" : 89,
#     "haider" : 56,
#     "abu bakar" : 78,
#     "naveen" : 82,
#     "sharoon" : 99,
#     "naveed" : 45,

# }
# students_grades ={}
# for student in student__marks:
#     score = student__marks[student]
#     if score > 90:
#         students_grades[student] = "outstandings. "
#     elif score > 80:
#         students_grades[student] = "Exceeds Expectations. "
#     elif score > 70:
#         students_grades[student] = "good. "
#     else: 
#         students_grades[student] = "fail. "
# print(students_grades)

# capitals = {
#     "pakistan" : "islamabad",
#     "india" : "mumbai",
#     "france" : "paris",
# } 
# visited_places = {
#     "pakistan" : ["islamabad","karachi","multan"],
#     "india" : {"dharmshala" : ["park","resturent","hotels"]}
# } 

# print(capitals.items())
# print(visited_places.items())

travel_logs = [
    {
        "country" : "france",
        "times" : 5,
        "places" : ["berlin","city"]
    },
     {
        "country" : "pakistan",
        "times" : 3,
        "places" : ["peshawar","okara","pindi"]
    },
]

def add_new_country(visited_country, visited_times, visited_city):
    new_country = {}
    new_country["country"] = visited_country
    new_country["times"] = visited_times
    new_country["places"] = visited_city
    
    travel_logs.append(new_country)

add_new_country("russia" , 2 , ["moscow","park"])
print(travel_logs)
