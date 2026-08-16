class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")

        for i in range(len(words) -1):
            if words[i][-1] != words[i + 1][0]:
                return False
            
        return sentence[-1] == sentence[0]

"""
Time Complexity : o(n)
Space Complexity : O(n)
"""