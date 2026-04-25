# Sort list of tuples using lambda

students = [("Amit", 85), ("Rahul", 90), ("Neha", 80)]

sorted_list = sorted(students, key=lambda x: x[1])

print(sorted_list)


'''output'''
[('Neha', 80), ('Amit', 85), ('Rahul', 90)]