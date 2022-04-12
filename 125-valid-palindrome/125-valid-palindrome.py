class Solution:
    def isPalindrome(self, s: str) -> bool:
        rebuild: str = ""
        
        for i in s:
            if i.isalnum():
                rebuild += i.lower()
        
        return True if rebuild == rebuild[::-1] else False
        
        