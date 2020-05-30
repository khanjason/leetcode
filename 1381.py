class CustomStack:

    def __init__(self, maxSize: int):
        self.maxsize=maxSize
        self.stack=[]
    def push(self, x: int) -> None:
        if len(self.stack)<self.maxsize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k<=len(self.stack):
            
            
            for item in range(0,k):
                self.stack[item]=self.stack[item]+val
                
        else:
            for t in range(0,len(self.stack)):
                self.stack[t]=self.stack[t]+val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
