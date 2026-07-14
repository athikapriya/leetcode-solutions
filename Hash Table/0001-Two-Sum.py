from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i in range(len(nums)):
            seen = target - nums[i]

            if seen in res:
                return [res[seen], i]
            
            res[nums[i]] = i


"""
LeetCode 1. Two Sum

Patterns:
- Array
- Hash Table

Time: O(n)
Space: O(n)
"""