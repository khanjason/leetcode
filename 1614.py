class Solution:
    def maxDepth(self, s: str) -> int:
        c=[0]
        curr=0
        for i in s:
            if i=='(':
                curr=curr+1
            if i==')':
                c.append(curr)
                curr=curr-1
        return max(c)
