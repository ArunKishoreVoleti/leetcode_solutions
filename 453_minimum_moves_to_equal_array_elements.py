from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Each move increments n - 1 elements by 1.
        This is equivalent to decrementing one element by 1 in reverse.
        To make all numbers equal to the minimum value, we just need to
        reduce the total sum by the amount needed to bring every element
        down to the minimum.

        Total moves = sum(nums) - min(nums) * len(nums)
        """
        return sum(nums) - min(nums) * len(nums)
