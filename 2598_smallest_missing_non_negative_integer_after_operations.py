from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        """
        Finds the smallest non-negative integer that cannot be represented as 
        nums[i] + k * value for any i and integer k.

        The logic:
        1. Compute remainder frequencies of each number in `nums` modulo `value`.
        2. Starting from 0, incrementally check integers to see if their remainder
           still has an available count.
        3. When a remainder runs out of counts, that integer is the answer.

        Args:
            nums (List[int]): List of integers.
            value (int): The divisor used to compute remainders.

        Returns:
            int: The smallest non-negative integer not representable
                 as nums[i] + k * value.
        """
        # Step 1: Count how many times each remainder (num % value) appears
        remainder_count: List[int] = [0] * value
        for num in nums:
            remainder = num % value
            remainder_count[remainder] += 1

        # Step 2: Start from 0 and find the first integer that can't be matched
        missing_integer: int = 0

        while True:
            remainder = missing_integer % value
            if remainder_count[remainder] > 0:
                # We can represent this integer; use one occurrence of this remainder
                remainder_count[remainder] -= 1
                missing_integer += 1
            else:
                # No available remainder means this integer can't be represented
                return missing_integer
