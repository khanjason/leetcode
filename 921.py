class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        curr=0
        c=0
        for i in S:
            
            if i==')':
                if curr==0:
                    c=c+1
                else:
                    curr=curr-1
            else:
                curr=curr+1
        return c+curr
