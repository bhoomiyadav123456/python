# Find pairs with given sum

nums = [1, 2, 3, 4, 5]
target = 6

pairs = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((nums[i], nums[j]))

print(pairs)


'''Output'''
[(1, 5), (2, 4)]
