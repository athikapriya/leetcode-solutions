from sortedcontainers import SortedList
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedList()

        for i, num in enumerate(nums):
            if i > indexDiff:
                window.remove(nums[i - indexDiff - 1])

            pos = window.bisect_left(num - valueDiff)
            if pos < len(window) and window[pos] <= num + valueDiff:
                return True
            
            window.add(num)

        return False

"""
Time Complexity : O(n log k)
Space Complexity : O(k)
"""