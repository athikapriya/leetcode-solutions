from typing import List

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def binary_search(find_first):
            left = 0
            right = len(nums) - 1
            res = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    if find_first:
                        right =  mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res

        first =  binary_search(True)
        last = binary_search(False)

        return [first, last]


"""
Time Complexity : O(log n)
Space Complexity : O(1)
"""