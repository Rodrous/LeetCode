class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        for i in s:
            if i in '({[':   #if we get a character ( In python even char is string ) which is there in the string ({[ , then append it to stack.
                stack.append(i)
            elif i is ')':
                if not stack or stack[-1] != '(':  # Here if stack is empty or last element of stack doesnot matches the corresponding closing element then return False
                    return False
                stack.pop()
            elif i is '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif i is ']':
                if not stack or stack[-1]!='[':
                    return False
                stack.pop()
                
        if not stack:
            return True
        else:
            return False