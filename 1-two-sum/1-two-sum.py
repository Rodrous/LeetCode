class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memoryDict: Dict = {}
        for i,j in enumerate(nums):
            if target - j in memoryDict:
                return [memoryDict[target-j],i]
            else:
                memoryDict[j] = i
                
        