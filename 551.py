class Solution:
    def checkRecord(self, s: str) -> bool:
        
        lastlate=0
        abcount=0
        for i in s:
            if i=='L' and lastlate==2:
                return False
            elif i=='L':
                lastlate=lastlate+1
            elif abcount==1 and i=='A':
                return False
            
            elif i=='A':
                abcount=abcount+1
                lastlate=0
            else:
                lastlate=0
        return True
