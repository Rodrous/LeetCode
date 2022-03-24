class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memoryDict: Dict = {}
        
        for i,j in enumerate(numbers):
            if target - j in memoryDict:
                return [memoryDict[target-j]+1,i+1]
            else:
                memoryDict[j] = i
        