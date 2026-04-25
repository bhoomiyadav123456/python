temps = [35, 42, 46, 39, 44, 30, 48]

print("Hottest Day: - temp_monitor.py:3", max(temps))
print("Coldest Day: - temp_monitor.py:4", min(temps))

extreme_days = len([t for t in temps if t > 40])

for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"

print("Extreme Days: - temp_monitor.py:12", extreme_days)
print("Updated Temperatures: - temp_monitor.py:13", temps)

#output:
# Hottest Day: - temp_monitor.py:3 48
# Coldest Day: - temp_monitor.py:4 30
# Extreme Days: - temp_monitor.py:12 3
# Updated Temperatures: - temp_monitor.py:13 [35, 42, 'Heat Alert', 39, 44, 30, 'Heat Alert']
