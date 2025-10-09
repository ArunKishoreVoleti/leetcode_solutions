from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Example:
            Input: "abcabcbb"
            Output: 3
            Explanation: The answer is "abc", with the length of 3.

        Args:
            s (str): Input string.

        Returns:
            int: Length of the longest substring without repeating characters.
        """

        # Dictionary to store the most recent index of each character
        visited: Dict[str, int] = {}
        
        # Left pointer of the current window
        left: int = 0
        
        # Variable to store the maximum length found
        max_length: int = 0

        # Iterate with right pointer
        for right in range(len(s)):
            char: str = s[right]

            # If character is already seen and within the current window,
            # move the left pointer to one position right of its previous index
            if char in visited and visited[char] >= left:
                left = visited[char] + 1
            else:
                # Update the maximum window size found so far
                max_length = max(max_length, right - left + 1)

            # Update the last seen index of the current character
            visited[char] = right

        # Return the length of the longest substring
        return max_length
