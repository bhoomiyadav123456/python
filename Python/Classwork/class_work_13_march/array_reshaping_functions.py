import numpy as np
#array
array1 = np.array([32,56,78,90,56,45,89,12])
print("First Array : - reshape:4")
print(array1)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - reshape:6")
#reshaping in order 4,2
array2 = array1.reshape(4,2)
print("Second Array : - reshape:9")
print(array2)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - reshape:11")
# reshaping the array into 3d array
array3 = array1.reshape(2,2,2)

print("Third Array : - reshape:15")
print(array3)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - reshape:17")
array4 = array1.reshape(1,1,8)
print("Fourth Array - reshape:19")
print(array4)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - reshape:21")
array5 = array1.reshape(1,2,4)
print("Fifth Array - reshape:23")
print(array5)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ - reshape:25")
array6 = array1.reshape(1,4,2)
print("Sixth Array - reshape:27")
print(array6)
average = np.mean(array1)
print(average)
print("standard deviation : - reshape:31" , np.std(array1))




'''output'''
First Array :
[32 56 78 90 56 45 89 12]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
Second Array :
[[32 56]
 [78 90]
 [56 45]
 [89 12]]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
Third Array :
[[[32 56]
  [78 90]]

 [[56 45]
  [89 12]]]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
Fourth Array
[[[32 56 78 90 56 45 89 12]]]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
Fifth Array
[[[32 56 78 90]
  [56 45 89 12]]]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
Sixth Array
[[[32 56]
  [78 90]
  [56 45]
  [89 12]]]
57.25
standard deviation : 25.85899263312475