class Solution:
    def findValidPair(self, s: str) -> str:
        count = [0] * 10

        for digit in s:
            count[int(digit)] += 1

        for i in range(len(s) - 1):
            a = int(s[i])
            b = int(s[i + 1])
            if a != b and count[a] == a and count[b] == b:
                return s[i:i + 2]
        
        return ""


"""
Time complexity : O(n)
Space  complexitty : O(1)
"""