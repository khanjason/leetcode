class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1=0
        
        t=1
        for i in num1[::-1]:
            n1=(n1+(int(i)*t))
            t=t*10
        print(n1)
        n2=0
        t=1
        for it in num2[::-1]:
            n2=(n2+(int(it)*t))
            t=t*10
        print(n2)
        return str(n2*n1)
