from typing import List 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left = 0
        total = sum(nums)

        for i in range(len(nums)):
            right = total - left - nums[i]

            if right == left:
                return i

            left += nums[i]

        return -1

"""
Time Complexity : O(n)
Space Complexity : O(1)
"""