###  leed code https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# ### 26. Remove Duplicates from Sorted Array

## sorted the array first and remove the duplicated elements



class Solution(object):
    def removeDuplicates(self, nums):

        if not nums:
            return 0
        
        # Sort the array first
        nums.sort()
        
        # Initialize the first pointer `i` to the first element.
        i = 0

        # Traverse the array with the second pointer `j`.
        # Go through the array with the second pointer `j`.
        for j in range(1, len(nums)):
            # If a new unique element is found (different from the element at `i`).
            if nums[j] != nums[i]:
                # Move the first pointer `i` to the next position.
                i += 1
                # Update the element at `i` with the new unique element found.
                nums[i] = nums[j]

                print(f'pointer i : {i}, pointer j : {j}')
        
        # The number of unique elements is `i + 1`.
                print(f'i+1 is {i+1}')

        return i + 1

# Example usage:
nums = [45, 45, 1, 3, 3, 3, 4, 5, 2, 2, 2, 5, 45]

solution = Solution()
k = solution.removeDuplicates(nums)

# Print the result
print("The number of unique elements is:", k)
print("The array after removing duplicates is:", nums[:k])

#### =================================================  ###

# Example usage:










