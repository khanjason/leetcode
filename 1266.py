class Solution:
    
    def calc(self,p1,p2):
        
        tot=max(abs(p1[0]-p2[0]),abs(p1[1]-p2[1]))
        return tot
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t=0
        for l in range(len(points)):
            if l<len(points)-1:
                t=t+self.calc(points[l+1],points[l])
        return t
