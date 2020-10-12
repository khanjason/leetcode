# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.li=iterator
        self.pointer=0
        self.lis=[]
        self.iniList()
    def iniList(self):
        while self.li.hasNext():
            self.lis.append(self.li.next())
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.lis[self.pointer]
        

    def next(self):
        """
        :rtype: int
        """
        t= self.lis[self.pointer]
        self.pointer=self.pointer+1
        return t

    def hasNext(self):
        """
        :rtype: bool
        """
        if (self.pointer<=len(self.lis)-1):
            return True
        return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
