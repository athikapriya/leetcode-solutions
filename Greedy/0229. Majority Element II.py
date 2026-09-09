from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        vote1 = 0
        vote2 = 0

        for num in nums:
            if num == candidate1 :
                vote1 += 1
            elif num == candidate2 :
                vote2 += 1
            elif vote1 == 0:
                candidate1 = num
                vote1 = 1
            elif vote2 == 0:
                candidate2 = num
                vote2 = 1 
            else:
                vote1 -= 1
                vote2 -= 1

        result = []

        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > len(nums) //3:
                result.append(candidate)

        return result


"""
Approach : Boyer-Moore Voting Algorithm

Time complexity : O(n)
Space complexity : O(1)
"""