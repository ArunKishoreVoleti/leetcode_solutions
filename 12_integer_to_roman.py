from typing import Dict

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Converts an integer to its Roman numeral representation.

        The approach:
        1. Decompose the number into place values (ones, tens, hundreds, thousands).
        2. For each place value, check if it directly matches a Roman numeral.
        3. If not, handle subtraction cases (like 4 -> IV, 9 -> IX) or build the numeral
           using the largest possible Roman symbols.
        
        Args:
            num (int): Integer between 1 and 3999 to convert.
        
        Returns:
            str: Roman numeral representation of the integer.
        """
        # Basic Roman numeral mappings
        roman_map: Dict[int, str] = {
            1: 'I', 5: 'V', 10: 'X', 50: 'L',
            100: 'C', 500: 'D', 1000: 'M'
        }

        # Step 1: Decompose num into place values
        digits = list(str(num))
        digits.reverse()  # Start from the least significant digit
        for i in range(len(digits)):
            digits[i] = int(digits[i]) * (10 ** i)
        digits.reverse()  # Restore original order

        roman_result = ""

        # Step 2: Convert each place value to Roman numeral
        for value in digits:
            if value in roman_map:
                # Direct match
                roman_result += roman_map[value]
            else:
                # Check subtraction cases (e.g., 4, 9, 40, 90, etc.)
                roman_keys = sorted(roman_map.keys(), reverse=True)
                flag = False
                for i in range(len(roman_keys)):
                    for j in range(i + 1, len(roman_keys)):
                        if abs(roman_keys[i] - roman_keys[j]) == value:
                            if roman_keys[j] < roman_keys[i]:
                                roman_result += roman_map[roman_keys[j]] + roman_map[roman_keys[i]]
                            else:
                                roman_result += roman_map[roman_keys[i]] + roman_map[roman_keys[j]]
                            flag = True
                if not flag:
                    # Build numeral using the largest possible symbols
                    remaining = value
                    usable_keys = sorted([k for k in roman_map if k <= remaining], reverse=True)
                    idx = 0
                    while remaining > 0:
                        if usable_keys[idx] <= remaining:
                            roman_result += roman_map[usable_keys[idx]]
                            remaining -= usable_keys[idx]
                        else:
                            idx += 1

        return roman_result
