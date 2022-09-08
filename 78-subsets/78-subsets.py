class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(stack,i):
            if i >= len(nums):
                result.append(stack.copy())
                return
            
            stack.append(nums[i])
            dfs(stack,i+1)
            stack.pop()
            dfs(stack,i+1)
        
        dfs([],0)
        return result