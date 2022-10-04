import numpy as np
# Find the positions of:
# elements in x where its value is more than its corresponding element in y, and
# elements in x where its value is equals to its corresponding element in y.

x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89])
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])
print("x =", x)
print("y =", y)
print("x > y =", np.where(x > y))
print("x == y =", np.where(x == y))


#Generate a 1-D array of 10 random integers. Each integer should be a number between 30 and
#40 (inclusive)
x = np.random.randint(low=30, high=40, size=10)
print(x)

# 3.Replace all odd numbers in the given array with -1

exercise_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Original array:")
print(exercise_1)
print("Replace all odd numbers of the said array with -1:")
exercise_1[exercise_1 % 2 == 1] = -1
print(exercise_1)
