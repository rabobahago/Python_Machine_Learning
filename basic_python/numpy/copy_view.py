# The Difference Between Copy and View
# The main difference between a copy and a view of an array is that the copy
# is a new array, and the view is just a view of the original array.
# The copy owns the data and any changes made to the copy will not
# affect original array, and any changes made to the original array will not affect the copy.
# The view does not own the data and any changes made to the view will
# affect the original array, and any changes made to the
# original array will affect the view.

# Make a copy, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# VIEW:
# Make a view, change the original array, and display both arrays:

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# Make Changes in the VIEW:
# Make a view, change the view, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

#Print the value of the base attribute to check if an array owns it's data or not:

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)