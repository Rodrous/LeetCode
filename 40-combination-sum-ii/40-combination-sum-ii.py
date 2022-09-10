class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(stack,index):
            
            if sum(stack) == target:
                res.append(stack.copy())
                return
            
            if sum(stack) > target or index+1 > len(candidates):
                return
            
            
            stack.append(candidates[index])
            dfs(stack,index+1)
            stack.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            
            dfs(stack,index+1)
        
        dfs([],0)
        return res