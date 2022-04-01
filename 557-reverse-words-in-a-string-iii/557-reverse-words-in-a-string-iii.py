class Solution:
    def reverseWords(self, s: str) -> str:
        resultant: str = []
        
        for i in s.split():
            resultant.append(i[::-1])
        return " ".join(resultant)
        