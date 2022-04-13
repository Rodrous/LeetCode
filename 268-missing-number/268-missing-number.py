class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        maxrange = max(nums)+2
        
        for i in range(0,maxrange):
            if i in nums:
                pass
            else:
                return i
         