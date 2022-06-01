class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        resultant: List = []
        digitMap: Dict = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }
            
        
        def backTrack(i: int, curStr: str):
            if len(curStr) == len(digits):
                resultant.append(curStr)
                return
            
            for c in digitMap[digits[i]]:
                backTrack(i+1,curStr + c)
        if digits:
            backTrack(0,"")
        
        return resultant
        