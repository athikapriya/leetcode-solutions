from typing import List 

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set()

        for path in paths:
            starts.add(path[0])

        for path in paths:
            if path[1] not in starts:
                return path[1]

"""
Time Complexity : O(n)
Space complexity : O(n)
"""