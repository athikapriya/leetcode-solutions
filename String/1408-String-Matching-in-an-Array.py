from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue

                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res


"""
Time complexity: O(n² × m)
    - n is the number of words.
    - m is the average length of a word (substring search takes up to O(m) on average, though the exact complexity depends on the language's implementation).

Space complexity: O(1)
    - auxiliary space (excluding the output list res).
"""
