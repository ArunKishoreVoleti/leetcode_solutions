from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # Precompute the length of the longest strictly increasing subarray starting at each index
        inc_len = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_len[i] = inc_len[i + 1] + 1

        max_k = 0
        # Check for each possible starting index a
        for a in range(n):
            k = inc_len[a]
            b = a + k
            if b < n and inc_len[b] >= k:
                max_k = max(max_k, k)

        return max_k
