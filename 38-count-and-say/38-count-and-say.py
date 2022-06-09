class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(2,n+1):
            res = ''.join([str(sum(1 for _ in l)) + el for el, l in groupby(res)])
        return res
            
        