class Solution:
    
    def gcd(self,a, b):
        while b != 0:
            t = b
            b = a % b
            a = t
        return a
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1=set(str1)
        s2=set(str2)
        if s1!=s2:
            
            return ""
        if str1 in str2:
            base=str1
            
        else:
            base=str2
        print(base)
        
        
        n=(self.gcd(len(str1),len(str2)))
        c=base[:n]
        count1=str1.count(c)
        if len(str1)/len(c)!=count1:
            return ""
        
        
        count2=str2.count(c)
        if len(str2)/len(c)!=count2:
            return ""
        return c
