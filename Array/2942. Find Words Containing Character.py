from typing import List 

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        for i, word in enumerate(words):
            if x in word:
                res.append(i)
        return res


'''
Time Complexity : O(n*m)
Space complexity : O(k)
'''