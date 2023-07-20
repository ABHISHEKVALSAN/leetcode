class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_index = []
        self.min_index = 0
        self.count = 0
        

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.min_index = self.count
            self.stack.append(val)
            self.stack_index.append(self.min_index)
        else:
            if self.stack[self.stack_index[-1]]>=val:
                print('p',self.stack,self.stack_index)
                self.min_index = self.count
            self.stack.append(val)
            self.stack_index.append(self.min_index)
        self.count+=1
        # print(self.stack)
        # print(self.stack_index)
        

    def pop(self) -> None:
        index = self.stack_index.pop()
        val = self.stack.pop()
        self.count-=1
        if len(self.stack)>0:
            self.min_index = min(self.min_index,self.stack_index[-1])
        else:
            self.min_index = 0
        # print(self.stack)
        # print(self.stack_index)
        return val
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.stack_index[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()