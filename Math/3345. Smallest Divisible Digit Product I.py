class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1

            for digit in str(n):
                product *= int(digit)

            if product % t == 0:
                return n

            n += 1

"""
Time Complexity : O(k × d)
where,
    k = number of integers checked until a valid one is found.
    d = number of digits in each integer.

Space Complexity : O(1)
"""