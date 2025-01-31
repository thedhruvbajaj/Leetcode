from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # Dictionary to store previously seen numbers and their indices  

        for i, n in enumerate(nums):  # Loop through the array  
            diff = target - n  # Compute the required difference  

            if diff in prevMap:  # Check if the difference exists in the hashmap  
                return [prevMap[diff], i]  # Return indices of the two numbers  

            prevMap[n] = i  # Store the current number and its index in the hashmap  
