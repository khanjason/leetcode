class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        
        self.store=[]
        self.pointer=0
        self.size=k
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.store)<self.size:
            v=[value]
            self.store=v+self.store
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.store)<self.size:
            v=[value]
            self.store=self.store+v
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.store)>0:
            
            self.store=self.store[1:]
            #pointer=pointer-1
            
            return True
        else:
            return False
        
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.store)>0:
            
            s=self.store.pop()
            #pointer=pointer-1
            
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.store==[]:
            return -1
        
        elif len(self.store)>0:
            return self.store[0]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.store==[]:
            return -1
        elif len(self.store)>0:
            return self.store[len(self.store)-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.store==[]:
            return True
        return False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.store)==self.size:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
