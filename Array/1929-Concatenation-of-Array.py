from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(2):
            for n in nums:
                res.append(n)
        return res

'''
Time Complexity : O(n)
Space Complexity : O(n)


Time :
Outer loop 2 times, inner loop n times
so 2xn = 2n 
O(n)

Space :
nums has n elements, res contains 2n elements.
O(2n) = O(n)
'''