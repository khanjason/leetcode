class Solution:
    def countSegments(self, s: str) -> int:
        if s=="":
            return 0
        c=0
        for i in s.split(' '):
            
            if i!=" " and i!='':
                c=c+1
        
        return (c)
