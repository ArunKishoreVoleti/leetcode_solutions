class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

        Steps:
            1. Ignore leading whitespace.
            2. Check for optional '+' or '-' sign.
            3. Read digits until a non-digit character is encountered.
            4. Convert the digits into an integer and apply the sign.
            5. Clamp the result within the 32-bit signed integer range.

        Args:
            s (str): Input string.

        Returns:
            int: Converted integer within the 32-bit signed integer range.
        """

        # Step 1: Trim leading spaces
        s = s.lstrip()

        # If string becomes empty, return 0
        if not s:
            return 0

        # Step 2: Check for sign
        sign: int = 1
        if s[0] in ('-', '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]  # Remove sign character for processing digits

        # Step 3: Extract continuous digits
        num_str: str = ""
        for char in s:
            if char.isdigit():
                num_str += char
            else:
                break  # Stop at first non-digit

        # If no digits were found, return 0
        if not num_str:
            return 0

        # Step 4: Convert to integer and apply sign
        num: int = sign * int(num_str)

        # Step 5: Clamp the integer to 32-bit signed range
        INT_MIN: int = -2**31
        INT_MAX: int = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        # Step 6: Return the final integer
        return num
