class Solution:
    def reverseParentheses(self, s: str) -> str:
        self.stack=[]
        self.string=""
        for i in range (len(s)):
            if s[i]=="(":
                self.stack.append(self.string)
                self.string=""
                
            elif s[i]==")":
                self.string=self.string[::-1]
                letter=self.stack.pop()
                
                self.string=letter +self.string

            else:
                self.string+=s[i]
          
        return self.string 
            