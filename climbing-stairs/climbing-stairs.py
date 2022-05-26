class Solution:
    def fib(self, n , dp):
        if n <= 1:
            return n
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.fib(n-1,dp) + self.fib(n-2,dp)
        
        return dp[n]
    
    def climbStairs(self,N):
        dp = [0]*(N + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[N]