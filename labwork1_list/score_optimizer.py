scores = [25, 32, 35, 40, 50, 60, 20]

# Remove lowest 2
scores.sort()
scores = scores[2:]

# Grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Count pass
passed = len([s for s in scores if s >= 40])

print("Updated Scores: - score_optimizer.py:15", scores)
print("Students Passed: - score_optimizer.py:16", passed)


#output:
# Updated Scores: - score_optimizer.py:15 [30, 35, 40, 50, 60]
# Students Passed: - score_optimizer.py:16 5    