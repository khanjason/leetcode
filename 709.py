class Solution:
    def toLowerCase(self, str: str) -> str:
        s=''
        cps=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        for t in str:
            if  t in cps:
                o=ord(t)+32
                s=s+chr(o)
            else:
                s=s+t
        return(s)
