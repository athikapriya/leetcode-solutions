from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []

        match = set(nums)

        for i in range(1, len(nums) + 1) :
            if i not in match:
                ans.append(i)
        
        return ans

"""
Time Complexity : O(n)
Space Complexity : O(n)
"""