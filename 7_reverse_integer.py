class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of a 32-bit signed integer.

        The function handles both positive and negative integers, 
        and ensures that the reversed integer remains within the 
        32-bit signed integer range. If it overflows, it returns 0.

        Args:
            x (int): The integer to be reversed.

        Returns:
            int: The reversed integer or 0 if it overflows.
        """

        # Define the 32-bit signed integer range
        INT_MIN: int = -2**31
        INT_MAX: int = 2**31 - 1

        # Determine the sign of the integer
        sign: int = -1 if x < 0 else 1
        x_abs: int = abs(x)

        # Reverse the digits of the absolute value
        reversed_x: int = 0
        while x_abs != 0:
            digit: int = x_abs % 10
            x_abs //= 10

            # Check for overflow before actually adding the digit
            if (reversed_x > INT_MAX // 10 or 
                (reversed_x == INT_MAX // 10 and digit > INT_MAX % 10)):
                return 0
            
            reversed_x = reversed_x * 10 + digit

        # Apply the original sign to the reversed integer
        reversed_x *= sign

        # Return the reversed integer if within bounds, else return 0
        return reversed_x if INT_MIN <= reversed_x <= INT_MAX else 0
