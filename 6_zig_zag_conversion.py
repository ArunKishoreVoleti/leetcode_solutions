class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts a given string into a zigzag pattern on a given number of rows.

        The function constructs the zigzag pattern by iterating through the 
        characters of the string and placing them in the appropriate row 
        based on the current direction (down or up).

        Args:
            s (str): Input string to be converted.
            numRows (int): Number of rows for the zigzag pattern.

        Returns:
            str: The string read line by line from the zigzag pattern.
        """

        # If numRows is 1 or greater than or equal to the length of s,
        # return the original string as no zigzag conversion is needed.
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize a list of strings for each row
        rows: list[str] = [''] * numRows
        current_row: int = 0
        going_down: bool = False

        # Iterate through each character in the string
        for char in s:
            # Append the character to the current row
            rows[current_row] += char
            
            # Change direction if we are at the first or last row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row based on the current direction
            current_row += 1 if going_down else -1

        # Join all rows to get the final converted string
        return ''.join(rows)