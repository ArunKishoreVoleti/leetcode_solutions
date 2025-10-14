from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        """
        Determines whether the given list of integers `nums` contains
        two consecutive increasing subarrays of at least length `k`.

        The function checks for overlapping increasing sequences
        in the array — i.e., sequences where each next number is 
        greater than the previous one. It maintains the lengths of 
        the current and previous increasing subarrays to find the
        maximum overlap possible.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The required minimum length of overlapping increasing subarrays.

        Returns:
            bool: True if such two consecutive increasing subarrays exist, False otherwise.
        """

        current_increase: int = 1      # Tracks length of current increasing subarray
        previous_increase: int = 0     # Tracks length of previous increasing subarray
        max_length: int = 0            # Stores maximum overlap found so far

        # Traverse array to find increasing sequences
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_increase += 1   # Continue increasing sequence
            else:
                previous_increase = current_increase  # Store completed sequence length
                current_increase = 1                  # Reset for next sequence

            # Update maximum overlap:
            # - (current_increase >> 1) is equivalent to floor(current_increase / 2)
            # - min(previous_increase, current_increase) gives overlap between sequences
            max_length = max(
                max_length,
                max(current_increase >> 1, min(previous_increase, current_increase))
            )

            # If the overlap length meets or exceeds k, return True
            if max_length >= k:
                return True

        # If no sufficient overlap found
        return False
