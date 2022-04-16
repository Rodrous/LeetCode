class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p: int = 0
        q: int = len(needle)-1
        
        while q <= len(haystack)-1:
            if haystack[p:q+1] == needle:
                return p
            p += 1
            q += 1
        return -1

        