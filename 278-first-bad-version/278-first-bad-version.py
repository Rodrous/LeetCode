# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        p: int = 1
        
        while n > p:
            mid = (p+n)//2
            if isBadVersion(mid):
                n = mid
            else:
                p = mid + 1
        return p
                
        