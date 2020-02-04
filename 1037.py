class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        #line is y=mx+c
        
        for t in points:
            if points.count(t)>1:
                return False
        
        
        
        y1=points[0][1]
        y2=points[1][1]
        y3=points[2][1]
        
        x1=points[0][0]
        x2=points[1][0]
        x3=points[2][0]
        
        if x1==x2==x3 or y1==y2==y3:
            return False
        
        elif x1==x2 or x2==x3 or x1==x3:
            return True
        
        m1=(y2-y1)/(x2-x1)
        m2= (y3-y2)/(x3-x2)
        m3=(y3-y1)/(x3-x1)
        
        
        if m1==m2==m3:
            return False
        else:
            return True
