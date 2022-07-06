class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            start, end = i[0],i[-1]
            
            if target == start:
                return True
            elif target == end:
                return True
            
            if target > start and target < end:
                return self.doBinarySearch(i, target)
    
    def doBinarySearch(self,targetList: List, target: int ) -> bool:
        p: int = 0
        q: int = len(targetList)-1
        
        while p <= q:
            mid = (p+q)//2
            
            if targetList[mid] == target:
                return True
            elif targetList[mid] > target:
                q = mid - 1
            else:
                p = mid + 1
        
        return False