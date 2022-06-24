class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_a : int = 0
        pointer_b : int = 0
        while pointer_b <= len(t)-1 and pointer_a <= len(s)-1:
            if s[pointer_a] == t[pointer_b]:
                pointer_a += 1
            
            pointer_b += 1
        return pointer_a == len(s)
        