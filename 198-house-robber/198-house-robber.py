class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache
        def dfs(n):

            if n >= len(nums):
                return 0

            return max(nums[n] + dfs(n+2), dfs(n+1))
        
        return dfs(0)
        
        
        
            
            
        