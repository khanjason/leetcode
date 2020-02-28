class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for item in moves:
            if item=='R':
                x=x+1
            if item=='L':
                x=x-1
            if item=='U':
                y=y+1
            if item=='D':
                y=y-1
        if x==0 and y==0:
            return True
        else:
            return False
