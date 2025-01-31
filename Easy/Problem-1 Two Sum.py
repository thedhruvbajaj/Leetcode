class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store previously seen numbers and their indices
        prevMap = {}  

        # Loop through the array
        for i, n in enumerate(nums):  
            # Compute the required difference
            diff = target - n  

            # Check if the difference exists in the hashmap
            if diff in prevMap:  
                # Return indices of the two numbers
                return [prevMap[diff], i]  

            # Store the current number and its index in the hashmap
            prevMap[n] = i  
