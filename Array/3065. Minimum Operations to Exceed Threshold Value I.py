from typing import List 

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        opt = 0

        for num in nums:
            if num < k:
                opt += 1
        return opt

"""
Time Complexity : O(n)
Space Complexity : O(1)
"""