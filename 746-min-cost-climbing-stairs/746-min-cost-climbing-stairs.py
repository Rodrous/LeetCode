class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache()
        def dfs(n):
            if n >= len(cost):
                return 0
            return cost[n] + min(dfs(n+1), dfs(n+2))
        
        return min(dfs(0),dfs(1))