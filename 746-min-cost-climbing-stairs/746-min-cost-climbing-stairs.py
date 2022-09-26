class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memory = {}
        def dfs(n):
            if n >= len(cost):
                return 0
            if n in memory:
                return memory[n]
            else:
                memory[n] = cost[n] + min(dfs(n+1), dfs(n+2))
            return memory[n]
        
        return min(dfs(0),dfs(1))