class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def robber(num):
            
            a,b = 0,0
            
            for i in num:
                temp = max(a+i ,b)
                a = b
                b = temp 
            return b
        
        return max(nums[0],robber(nums[1:]),robber(nums[:-1]))