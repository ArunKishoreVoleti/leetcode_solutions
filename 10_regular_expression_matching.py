import re
from typing import Pattern

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Implements regular expression matching using Python's re module.

        Example:
            Input: s = "aa", p = "a*"
            Output: True
            Explanation: The pattern "a*" matches "aa".

        Args:
            s (str): Input string to be matched.
            p (str): Pattern string which may contain regex operators (like '.', '*').

        Returns:
            bool: True if the entire string matches the pattern, False otherwise.
        """

        # Compile the given pattern for efficiency and clarity
        pattern: Pattern[str] = re.compile(p)

        # Perform a full match to ensure the entire string matches the pattern
        match_result = re.fullmatch(pattern, s)

        # Return True if a match object is found, else False
        return match_result is not None
