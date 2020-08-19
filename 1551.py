class Solution(object):
   
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=n/2
        return count*(count+n%2)
        
