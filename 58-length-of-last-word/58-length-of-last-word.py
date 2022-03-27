class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s: str = s[::-1]
        size: int = 0
        if len(s) == 1: return 1
        for j,i in enumerate(s):
            if i == " ":
                pass
            else:
                if i != " ":
                    size += 1
                    if j+1 < len(s)-1 and s[j+1] == " ":
                        return size
        return size
                
                
                
        