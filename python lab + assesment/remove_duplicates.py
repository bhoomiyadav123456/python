# Remove duplicates while maintaining order

nums = [1, 2, 2, 3, 4, 3, 5]

result = []

for num in nums:
    if num not in result:
        result.append(num)

print(result)


'''output'''
[1, 2, 3, 4, 5]
