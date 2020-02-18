class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        tot=0
        for t in grid:
            for item in t:
                if item<0:
                    tot=tot+1
        return(tot)
