class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for i in range(len(s) - 1):
            res += abs(ord(s[i]) - ord(s[i + 1]))

        return res

"""
Time Complexity : O(n)
Space Complexity : O(1)
"""