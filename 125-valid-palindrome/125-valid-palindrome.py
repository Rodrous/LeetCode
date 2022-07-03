class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr_a : int = 0
        ptr_b : int = len(s)-1
        
        while ptr_b >= ptr_a:
            if not s[ptr_a].isalnum():
                
                ptr_a+=1
            elif not s[ptr_b].isalnum():
                ptr_b-=1
            
            else:
                if s[ptr_a].lower() != s[ptr_b].lower():
                    return False
                
                ptr_a+=1
                ptr_b-=1
        
        return True
        