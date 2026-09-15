from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        positive = set()

        for num in nums:
            if num > 0:
                positive.add(num)

        return len(positive)


"""
Time Complexity : O(n)
Space Complexity : O(n)
"""