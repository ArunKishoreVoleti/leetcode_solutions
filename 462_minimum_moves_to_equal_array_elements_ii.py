from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
        Finds the minimum moves needed to make all values equal.

        The approach:
        1. Sort the numbers and select a median.
        2. Sum each number's distance from the median.

        Choosing a median minimizes the total absolute difference, and each
        move changes one number by 1.

        Args:
            nums (List[int]): List of integers to make equal.

        Returns:
            int: The minimum number of moves required.
        """
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(num - median) for num in nums)
