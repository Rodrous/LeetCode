class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        resultant: List[List] = [[1]]
        
        for i in range(numRows-1):
            temp = [0] + resultant[-1] + [0]
            row = []
            for j in range(len(resultant[-1])+1):
                row.append(temp[j] + temp[j+1])
            resultant.append(row)
        return resultant
        