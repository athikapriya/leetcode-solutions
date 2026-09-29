
def isBadVersion(version):
    return version >= 4

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right =  n

        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return left


"""
Time Complexity : O(log n)
Space Complexity : O(1)
"""