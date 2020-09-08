import math
class Solution(object):
    def frombin(self,n):
        return int(n,2) 
            
        
    def tobin(self,n):
        return bin(n).replace("0b","") 
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
    
        s=self.frombin(a)+self.frombin(b)
        return(self.tobin(s))
