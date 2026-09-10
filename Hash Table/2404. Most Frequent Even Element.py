from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0) + 1

        ans = -1
        max_freq = 0

        for num, frequency in freq.items():
            if frequency > max_freq:
                max_freq = frequency
                ans = num
            elif frequency == max_freq and num < ans:
                ans = num

        return ans

"""
Time Complexity : O(n)
Space Complexity  : O(n)
"""