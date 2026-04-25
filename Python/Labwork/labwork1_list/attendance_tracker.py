attendance = [1, 1, 0, 0, 1, 0, 0, 0, 1]

percentage = (sum(attendance) / len(attendance)) * 100
print("Attendance %: - attendance_tracker.py:4", percentage)

if percentage < 75:
    print("Below 75% Attendance - attendance_tracker.py:7")

# Replace consecutive absences
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "Warning"

print("Updated Attendance: - attendance_tracker.py:14", attendance)

#output:
# Attendance %: - attendance_tracker.py:4 44.44444444444444
# Below 75% Attendance - attendance_tracker.py:7
# Updated Attendance: - attendance_tracker.py:14 ['Warning', 1, 0, 'Warning', 1, 0, 0, 0, 1]