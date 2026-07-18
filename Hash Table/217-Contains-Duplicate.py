from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
            
        return False
    

"""
Time Complexity : 
- n = len(nums)
- Creating the empty set: O(1)
- The loop runs at most n times.
- For each element:
   - n in hashset → O(1) average
   - hashset.add(n) → O(1) average

So the total work is:
    n × (O(1) + O(1))
    = O(n)

Time : 
- Best Case: O(1)
- Worst/Average Case: O(n)

Space Complexity : O(n)
"""