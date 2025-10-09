from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays.

        The function merges both arrays, sorts the combined array, 
        and then returns the median value.

        Args:
            nums1 (List[int]): First sorted list of integers.
            nums2 (List[int]): Second sorted list of integers.

        Returns:
            float: Median of the two sorted arrays.
        """

        # Combine both sorted arrays
        nums: List[int] = nums1 + nums2

        # Sort the combined list
        nums.sort()

        # Get total number of elements
        n: int = len(nums)

        # If number of elements is odd, return the middle element
        if n % 2 == 1:
            median: float = float(nums[n // 2])
        else:
            # If even, average the two middle elements
            median: float = (nums[n // 2 - 1] + nums[n // 2]) / 2
        
        # Return the computed median
        return median
