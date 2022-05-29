import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res: List = [1] * (len(nums))
        prefix: int = 1
        
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix: int = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res