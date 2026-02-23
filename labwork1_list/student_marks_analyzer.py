marks = [95, 102, 67, -5, 88, 76, 100, 45]

# Remove invalid marks
valid_marks = [m for m in marks if 0 <= m <= 100]

# Calculate average
average = sum(valid_marks) / len(valid_marks)

# Find topper(s)
highest = max(valid_marks)
toppers = [m for m in valid_marks if m == highest]

# Grade based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "D"

print("Valid Marks: - student_marks_analyzer.py:23", valid_marks)
print("Average: - student_marks_analyzer.py:24", average)
print("Topper Marks: - student_marks_analyzer.py:25", toppers)
print("Grade: - student_marks_analyzer.py:26", grade)

#output:
# Valid Marks: - student_marks_analyzer.py:23 [95, 102, 67, -5, 88, 76, 100, 45]
# Average: - student_marks_analyzer.py:24 81.42857142857143 
# Topper Marks: - student_marks_analyzer.py:25 [102]
# Grade: - student_marks_analyzer.py:26 B  