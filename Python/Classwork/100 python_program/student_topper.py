n = int(input("Enter number of students: "))
students = {}

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

topper = max(students, key=students.get)

print("Topper: - student_topper.py:11", topper)
print("Marks: - student_topper.py:12", students[topper])



'''Output:'''
Enter number of students: 2
Enter student name: Ravi
Enter marks: 85
Enter student name: Aman
Enter marks: 92
Topper: Aman
Marks: 92