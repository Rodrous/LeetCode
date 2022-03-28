class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result: List[List] = [[1]]
        for i in range(rowIndex):
            temp = [0]+ result[-1]+ [0]
            res = []
            for j in range(len(result[-1])+1):
                res.append(temp[j]+temp[j+1])
            result.append(res)
        return result[-1]