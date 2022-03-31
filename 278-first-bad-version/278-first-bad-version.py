# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        p = 1
        q = n
        while p < q:
            mid = (p + q)//2
            
            if isBadVersion(mid) == True:
                q = mid
            else:
                p = mid + 1
        return p
            
            