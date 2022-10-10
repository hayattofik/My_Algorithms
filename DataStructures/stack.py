from inspect import stack
from operator import truediv


class Stack:
    def __init__(self) :
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
        return self.stack
    def pop():
        if self.is_Empty():
            return "Empty stack can not be poped"
        else:
            self.stack.pop()
            return self.stack
    def is_Empty():
        if not Stack==True:
            return True
        else:
            return False
    def top():
        if self.is_Empty():
            return "Empty stack "
        else:
            return self.stack[-1]
    def size():
        return len(stack)
    def diplay():
        print(self.stack)
stack=Stack()
stack.push(1)
stack.diplay()


# print(stack)
# print(stack.top())
# print(stack.size())
# print(stack.is_Empty())

