class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determines whether a given integer is a palindrome.

        A palindrome number reads the same backward as forward.

        Example:
            Input: 121
            Output: True
            Explanation: 121 reads the same from left to right and right to left.

        Args:
            x (int): Input integer.

        Returns:
            bool: True if the integer is a palindrome, False otherwise.
        """

        # ------------------------------------
        # Approach 1: String-based (Simple)
        # ------------------------------------
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        #
        # return str(x) == str(x)[::-1]


        # ------------------------------------
        # Approach 2: Math-based (Optimized)
        # ------------------------------------
        # Time Complexity: O(log10(n))
        # Space Complexity: O(1)
        #
        # Logic:
        #   - Compare the most significant (left) and least significant (right) digits.
        #   - Remove them from the number and continue inward.
        #   - Stop when all digits are checked.
        
        if x < 0:
            return False  # Negative numbers are never palindromes

        div: int = 1
        # Find the divisor to extract the leftmost digit
        while x // div >= 10:
            div *= 10

        # Compare digits from both ends
        while x:
            left: int = x // div
            right: int = x % 10

            if left != right:
                return False  # Mismatch found

            # Remove left and right digits
            x = (x % div) // 10
            div //= 100  # Adjust divisor after removing two digits

        return True
