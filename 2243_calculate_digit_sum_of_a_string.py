class Solution:
    def digitSum(self, s: str, k: int) -> str:
        """
        Repeatedly splits `s` into groups of `k` digits, sums each group,
        and concatenates the sums until the resulting string has at most
        `k` characters.

        Args:
            s (str): The input string of digits.
            k (int): The maximum number of digits in each group.

        Returns:
            str: The digit-sum string after all required transformations.
        """
        while len(s) > k:
            parts = []
            for i in range(0, len(s), k):
                chunk_sum = sum(int(digit) for digit in s[i:i + k])
                parts.append(str(chunk_sum))
            s = "".join(parts)

        return s
