# # PART I: Outputs first and last names of dict.
students = [
{'first_name': 'Michael', 'last_name': 'Jordan'},
{'first_name': 'John', 'last_name': 'Rosales'},
{'first_name': 'Mark', 'last_name': 'Guillen'},
{'first_name': 'KB', 'last_name': 'Tonel'}
]
def student_fullname(arr):
    for value in students:
        print value['first_name'],value['last_name']

student_fullname(students)

print "-------------"
# PART II: Create a program that prints the following format (including number
# of characters in each combined name):

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
count_students = 0
count_instructors = 0

for key,data in users.items():
    print key
    for value in data:
        if value == "Students":
            count_students += 1
        print count_students,"-",value["first_name"].upper(), value["last_name"].upper(),"-",len(value["last_name"])+len(value["first_name"])
