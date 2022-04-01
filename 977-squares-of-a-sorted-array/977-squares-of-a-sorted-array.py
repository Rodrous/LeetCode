class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        resultant: List = []
        p: int = 0
        q: int = len(nums)-1
        
        while p <= q:
            if abs(nums[p]) < abs(nums[q]):
                resultant.append(nums[q]**2)
                q-=1
            else:
                resultant.append(nums[p] ** 2)
                
                p+=1
        return resultant[::-1]
                
            