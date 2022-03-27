class Solution:
    def frequencySort(self, s: str) -> str:
        memoryDict : Dict = {}
        for i in s:
            if i in memoryDict:
                memoryDict[i] +=1
            else:
                memoryDict[i] = 1
        
        resultant: str = ""
        temp = sorted(memoryDict, key=memoryDict.get)
        for i in temp:
            multiplier = memoryDict[i]
            resultant += i*multiplier
        return resultant[::-1]