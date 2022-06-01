class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result: List = []
        digitMap: Dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backTrack(i: int, solStr: str) -> None:
            if len(solStr) == len(digits):
                result.append(solStr)
                return 
            
            for char in digitMap[digits[i]]:
                backTrack(i+1, solStr+char)
        
        if digits:
            backTrack(0,"")
        
        return result