from typing import List

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()

        res = []

        for i, num in enumerate(nums):
            if num == target:
                res.append(i)

        return res

"""
Time Complexity: O(n log n)
Space Complexity : O(n)
"""