# Assignment 6:-  Numpy

import numpy as np


# # #  Given an array a = np.array([10, 20, 30, 40, 50]) and 
# # # an index array i = np.array([0, 1, 3]), use fancy indexing 
# # # to extract elements and assign new values to them. 

# # Define the array
# a = np.array([10, 20, 30, 40, 50])

# # Define the index array
# i = np.array([0, 1, 3])

# # Extract elements using fancy indexing
# extracted_elements = a[i]

# # Assign new values to the extracted elements
# extracted_elements[:] = 999

# # Assign the modified elements back to the original array
# a[i] = extracted_elements

# print(a)

# #  Create a 4x4 matrix and compute the sum of all elements, the sum 
# # of each column, and the sum of each row.  

# # Create a 4x4 matrix
# matrix = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16] ])

# # Compute the sum of all elements
# total_sum = np.sum(matrix)

# # Compute the sum of each column
# column_sums = np.sum(matrix, axis=0)

# # Compute the sum of each row
# row_sums = np.sum(matrix, axis=1)

# print("Matrix:")
# print(matrix)
# print("\nTotal sum of all elements:", total_sum)
# print("Sum of each column:", column_sums)
# print("Sum of each row:", row_sums)

# Given a 3-D array of shape (3, 4, 5), slice out a sub-array that 
# contains the last two rows and columns of the last two matrices. 

# Step 1: Create a 3-D array of shape (3, 4, 5)
array = np.arange(60).reshape(3, 4, 5)

# Step 2: Slice out the sub-array
sub_array = array[-2:, -2:, -2:]

print("Original array:")
print(array)
print("\nSliced sub-array:")
print(sub_array)
