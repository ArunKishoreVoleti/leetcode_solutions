from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two distinct indices in the list 'nums' such that 
        the sum of the elements at those indices equals the target.

        Args:
            nums (List[int]): A list of integers.
            target (int): The target sum.

        Returns:
            List[int]: A list containing the two indices that add up to target.
                       Returns an empty list if no such pair exists.
        """

        # -----------------------------
        # Approach 1: Memory Optimized (Brute Force)
        # -----------------------------
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        #
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # -----------------------------
        # Approach 2: Time Optimized (Using Hash Map)
        # -----------------------------
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        mapping: dict[int, int] = {}  # Stores number -> index
        
        for i in range(len(nums)):
            rem: int = target - nums[i]  # Required complement
            
            # If complement already exists, return the pair of indices
            if rem in mapping:
                return [i, mapping[rem]]
            
            # Otherwise, store the current number with its index
            mapping[nums[i]] = i
        
        # Return empty list if no valid pair found
        return []
