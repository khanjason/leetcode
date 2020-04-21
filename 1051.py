class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s=sorted(heights)
        c=0
        for i in range(0,len(heights)):
            if s[i]!=heights[i]:
                c=c+1
        return c
