class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer: int = 0
        
        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums):
                if i != j:
                    possible = (val1-1)*(val2-1)
                    answer = max(possible,answer)
        return answer