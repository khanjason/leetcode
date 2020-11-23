class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        m=0
        start=-1
        li=[]
        for box in points:
            li.append(box[0])
        
        for i in li:
            if start==-1:
                start=i
            else:
                d=i-start
                if d>m:
                    m=d
                start=i
        return m
                    
