def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        num=self.stack[0]
        self.stack.remove(num)
        return num
        

    def peek(self) -> int:
        num=self.stack[0]
        return num 

    def empty(self) -> bool:
        print(self.stack)
        if len(self.stack)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()