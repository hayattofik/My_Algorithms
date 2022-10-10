class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pareth={")":"(","}":"{","]":"["}
      
        for i in s:
            if i in pareth.values():
                stack.append(i)
            elif stack and pareth[i]==stack[-1]:
                stack.pop()
            else:
                return False
        if stack==[]:
            return True
        else:
            return False
            
       