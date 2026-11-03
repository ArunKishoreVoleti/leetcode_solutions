from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Finds the minimum moves needed to make all values equal.

        The approach:
        1. Choose the largest value as the target.
        2. Sum the increments needed to bring each value to the target.

        Incrementing each value to the maximum minimizes the total number of
        moves when each move increases one value by 1.

        Args:
            nums (List[int]): List of integers to make equal.

        Returns:
            int: The minimum number of moves required.
        """
        target = max(nums)
        return sum(target - num for num in nums)
