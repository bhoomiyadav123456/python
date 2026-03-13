import numpy as np
#creating array
numbers1=np.array([45,78,90])
print ("array - numpy_basic_operation.py:4")
print(numbers1)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:6")
print("")
#second array
numbers2=np.array([45,3.5,90])
print("Array - numpy_basic_operation.py:10")
print(numbers2)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:12")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:13")
#third array
numbers3=np.array([45,3.5,90,'hello'])
print ("Array - numpy_basic_operation.py:16")
print(numbers3)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:18")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:19")
#multiply these elements by 3
print("After multiplying by 3: - numpy_basic_operation.py:21")
print(numbers1*3)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:23")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:24")
#elements greater than 70
print("Elements greater than 70 - numpy_basic_operation.py:26")
print(numbers1>70)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:28")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:29")
#Double dimensionAL array
matrix1=np.array([[45,67,89],[56,90,78]])
print("2D MATRIX - numpy_basic_operation.py:32")
print(matrix1)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:34")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:35")
#3d array
array3d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("3d array - numpy_basic_operation.py:38")
print(array3d)
print("_ _ _ _ _ _ _   _ _ _ _ _ _ - numpy_basic_operation.py:40")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:41")
#creating array
number5=np.array([45,67,89,4,34,])
print("Array : - numpy_basic_operation.py:44")
print(number5)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:46")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ - numpy_basic_operation.py:47")
#multiplying each element by 10
print("After multiplying by 10 - numpy_basic_operation.py:49")
print(number5*10)

'''output:

array
[45 78 90]
------------------
------------------
Array
[45.   3.5 90. ]
------------------
------------------
Array
['45' '3.5' '90' 'hello']
------------------
------------------
After multiplying by 3:
[135 234 270]
------------------
------------------
Elements greater than 70
[False  True  True]
------------------
------------------
2D MATRIX
[[45 67 89]
 [56 90 78]]
------------------
------------------
3d array
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
------------------
------------------
Array :
[45 67 89  4 34]
------------------
------------------
After multiplying by 10
[450 670 890  40 340]
'''