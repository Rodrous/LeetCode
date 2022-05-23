class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseMedaddy(s,0,len(s)-1)
        
    
    def reverseMedaddy(self,s: List[str], p:int , q:int) -> None:
        if p == q or q < p:
            return
        
        s[q],s[p] = s[p],s[q]
        p+=1
        q-=1
            
        return self.reverseMedaddy(s,p,q)
            
        