from typing import List 

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for _ in range(rowIndex):
            new_row = [1]

            for i in range(1, len(row)):
                new_row.append(row[i - 1] + row[i])

            new_row.append(1)
            row = new_row

        return row

"""
This solution follows Dynamic Programming Technique

Time Complexity : O(n²)
Space Complexity :O(n)
"""


"""
This cal also be solved with Mathematical / Combinatorics technique → Binomial Coefficients
Where the Time and Space both is O(n)

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        value = 1

        for k in range(1, rowIndex + 1):
            value = value * (rowIndex - k + 1) // k
            row.append(value)

        return row

"""