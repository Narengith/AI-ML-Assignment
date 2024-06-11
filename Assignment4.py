# Assignment 4:-

import numpy as np

def analyze_last_row(arr):

    # Select the last row
    last_row = arr[-1]
    
    # Calculate the average
    average = np.mean(last_row)
    
    # Find the minimum value
    minimum = np.min(last_row)
    
    # Find the maximum value
    maximum = np.max(last_row)
    
    # Count the number of even values
    num_evens = np.sum(last_row % 2 == 0)
    
    return average, minimum, maximum, num_evens

# Create a NumPy array with random values and shape it to (12, 5)
arr = np.random.randint(1, 100, (12, 5))

# Pass the array to the function
average, minimum, maximum, num_evens = analyze_last_row(arr)

# Print the array and the results
print("Array:")
print(arr)
print("\nAnalysis of the last row:")
print(f"Average -> {average}")
print(f"Minimum -> {minimum}")
print(f"Maximum -> {maximum}")
print(f"No. of evens -> {num_evens}")

# Define the array
arr = np.array([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9] ])

# Reverse the order of elements in each row
reversed_arr = arr[:, ::-1]

# Print the original and reversed arrays
print("Original array:")
print(arr)
print("\nReversed array:")
print(reversed_arr)
