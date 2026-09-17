from typing import List 

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        count = {}
        ans = 0

        for player, color in pick:
            if player not in count:
                count[player] = {}
            if color not in count[player]:
                count[player][color] = 0
            count[player][color] += 1 

        for player in count:
            for color in count[player]:
                if count[player][color] > player:
                    ans += 1
                    break

        return ans

"""
Time Complexity : o(m)
Space Complexity : O(m)
"""