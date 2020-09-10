class Solution(object):
  
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr=sorted([(bin(t).count('1'),t) for t in arr ])
        return [t[1] for t in arr]
