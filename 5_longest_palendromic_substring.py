class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in the given string.

        The function uses a center expansion technique to find the longest 
        palindromic substring by expanding around each character and its 
        adjacent character.

        Args:
            s (str): Input string.

        Returns:
            str: The longest palindromic substring.
        """

        def expand_around_center(left: int, right: int) -> str:
            """
            Expands around the center and returns the longest palindrome.

            Args:
                left (int): Left index of the center.
                right (int): Right index of the center.
            Returns:
                str: The longest palindromic substring found by expanding.
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest_palindrome: str = ""
        for i in range(len(s)):
            # Check for odd-length palindromes
            odd_palindrome: str = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            
            # Check for even-length palindromes
            even_palindrome: str = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome
