class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # y= mx +c
        #m = y2-y1 / x2 -x1
        mlist=[]
        for i in range(1,len(coordinates)):
            y2=coordinates[i][1]
            y1=coordinates[0][1]
            x2=coordinates[i][0]
            x1= coordinates[0][0]
            if x1==x2:
                return False
            m=((y2-y1)/(x2-x1))
        
            mlist.append(m)
        for thing in mlist:
            if thing!=m:
                return False
        return True
