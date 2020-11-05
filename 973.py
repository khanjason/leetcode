class Solution:
    
    def calcpy(self,p):
        p1=p[0]
        p2=p[1]
        return p1**2+p2**2
   

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda p:self.calcpy(p))
        return points[:K]
