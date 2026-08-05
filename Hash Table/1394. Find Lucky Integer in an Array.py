from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        ans = -1

        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
            
        for num, count in freq.items():
            if num == count :
                ans = max(ans, num)
        
        return ans

"""
Time Complexity: O(n)
Space Complexity : O(n)
"""