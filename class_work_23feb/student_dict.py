student = {}
#to insert an element
student['name'] = 'John'
student['roll'] = 43
student['age'] = 23

print(student)

student["english"] = 85
student["roll"] = 1024

print(student)

for key in student:
    print("key - student_dict.py:15", key, "value", student[key])

    #output:
# {'name': 'John', 'roll': 43, 'age': 23}
# {'name': 'John', 'roll': 1024, 'age': 23, 'english': 85}
# key - student_dict.py:15 name value John
# key - student_dict.py:15 roll value 1024
# key - student_dict.py:15 age value 23
# key - student_dict.py:15 english value 85 