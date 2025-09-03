###  leed code https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# ### 26. Remove Duplicates from Sorted Array

from typing import List

# Initialize the list with duplicates
nums2: List[int] = [45, 45, 12,1, 31, 31, 5,  12, 31, 12, 5, 45]

# Sort the array first
nums2.sort()
print(f'\nOriginal is {nums2}\n')

# Define a function named 'removeDuplicates2' that takes a list of integers as input and returns an integer.
def removeDuplicates2(nums2: List[int]) -> int:
    # Initialize a variable 'i' to 0. This will be used as an index to keep track of the position in the list.
    i = 0
    # Loop through each number 'num2' in the input list 'nums2'.
    for num2 in nums2:
        print(f'num {num2} and array {nums2}')
        # Check if 'i' is 0 (meaning this is the first element) or if 'num2' is greater than the previous element in the list.
        if i == 0 or num2 > nums2[i - 1]:
            # If the condition is true, assign the current number 'num2' to the 'i'th position in the list.
            nums2[i] = num2
            print(f'num is {num2}')
            # Increment 'i' by 1 to move to the next position in the list.
            i += 1
            print(f'increment of i  {i}')

    # Return the value of 'i', which represents the number of unique elements in the list.
    return i

# Print a message to indicate the start of the output.
print("Answer")

# Call the 'removeDuplicates2' function with a list 'nums2' (which is not defined in this code snippet) and store the result in 'k'.
k = removeDuplicates2(nums2)
# Print the number of unique elements in the list.
print("\nThe number of unique elements is:", k)
# Print the list with duplicates removed, up to the 'k'th position.
print("\nThe array after removing duplicates is:", nums2[:k])

#### =================================================  ###

# Example usage:
2




# nums2 : list = [45, 45, 1, 3, 3, 3, 4, 5, 2, 2, 2, 5, 45]
# # Sort the array first
# num2 =  nums2.sort()

# def removeDuplicates2(self, nums2: List[int]) -> int:
  
#     i = 0

#     for num2 in nums2:
#       if i < 1 or num2 > nums2[i - 1]:
#         nums2[i] = num2
#         i += 1

#     return i
# print("\nNum2 Answer" )

# # Call the function and print the result
# k = removeDuplicates2(nums2)
# print("The number of unique elements is:", k)
# print("The array after removing duplicates is:", nums2[:k])


