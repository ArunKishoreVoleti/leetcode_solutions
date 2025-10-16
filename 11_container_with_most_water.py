from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Calculates the maximum area of water that can be contained
        between two vertical lines represented by the `height` array.

        The approach uses the two-pointer technique:
        - Start with pointers at both ends.
        - Compute the area formed by the two lines.
        - Move the pointer pointing to the shorter line inward,
          since the limiting factor is the smaller height.

        Args:
            height (List[int]): List of non-negative integers representing line heights.

        Returns:
            int: The maximum area of water that can be contained.
        """
        left_pointer: int = 0
        right_pointer: int = len(height) - 1
        max_water_area: int = 0

        # Move two pointers towards each other
        while left_pointer < right_pointer:
            # Calculate the width and effective height
            width = right_pointer - left_pointer
            min_height = min(height[left_pointer], height[right_pointer])

            # Compute area for current pair of lines
            current_area = width * min_height
            max_water_area = max(max_water_area, current_area)

            # Move pointer of smaller line inward
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water_area
