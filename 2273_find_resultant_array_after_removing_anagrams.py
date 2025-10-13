from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        Removes consecutive anagrams from the given list of words.
        
        Args:
            words (List[str]): A list of lowercase words.
        
        Returns:
            List[str]: A list with consecutive anagrams removed.
        
        Example:
            Input: ["abba", "baba", "bbaa", "cd", "cd"]
            Output: ["abba", "cd"]

        My Leetcode Solution Approach: https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/solutions/7271599/simple-approach-remove-anagrams-in-an-ar-r2py/
        """
        
        result: List[str] = []   # Final list to store non-anagram words
        prev: str = ""           # Keeps track of the previous word in sequence
        
        for word in words:
            # Compare sorted characters of current word and previous word
            # If they are not the same, it means they are not anagrams
            if sorted(word) != sorted(prev):
                result.append(word)  # Add current word to the result list
                prev = word          # Update previous word tracker
                
        return result  # Return the filtered list of words
