class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPoint = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] + i >= lastPoint:
                lastPoint = i
        
        return lastPoint == 0