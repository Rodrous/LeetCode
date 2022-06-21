import operator
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        memoryDict: Dict = {}
        for i in nums:
            if i in memoryDict:
                memoryDict[i] += 1
            else:
                memoryDict[i] = 1

        
        return list(dict(sorted(memoryDict.items(), key=operator.itemgetter(1),reverse=True)).keys())[0:k]
        
        