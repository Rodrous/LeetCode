class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        p: int = 0
        q: int = len(nums)-1
        
        while p <= q:
            mid = (p+q)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                q = mid -1
            else:
                p = mid + 1
            
        return p
            
        