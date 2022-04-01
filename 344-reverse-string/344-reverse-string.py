class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p: int = 0
        q: int = len(s)-1
        
        while p <= q:
            s[p], s[q] = s[q],s[p]
            p+=1
            q-=1