points = [10, -5, 25, 18, 30, 22]

# Replace negative
points = [p if p >= 0 else 0 for p in points]

points.sort(reverse=True)

winner = points[0]
runner_up = points[1]

print("Leaderboard: - tournament_points.py:11", points)
print("Winner Points: - tournament_points.py:12", winner)
print("Runnerup Points: - tournament_points.py:13", runner_up)

#output:
# Leaderboard: - tournament_points.py:11 [30, 25, 22, 18, 10, 0]
# Winner Points: - tournament_points.py:12 30
# Runnerup Points: - tournament_points.py:13 25