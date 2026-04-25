salaries = [25000, 60000, 45000, 80000, 15000]

# Remove below minimum wage (20000)
salaries = [s for s in salaries if s >= 20000]

# Add 5% bonus
salaries = [s*1.05 if s > 50000 else s for s in salaries]

# Sort descending
salaries.sort(reverse=True)

print("Top 3 Salaries: - salary_processing_system.py:12", salaries[:3])

#output:
# Top 3 Salaries: - salary_processing_system.py:12 [84000.0, 47250.0, 26250.0]