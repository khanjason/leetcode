class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        p=1/n
        
        for i in range(1,n):
            p=0.5
        return p
