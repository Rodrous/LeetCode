class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted([i for i in s])
        t = sorted([i for i in t])
        
        return s==t 
        