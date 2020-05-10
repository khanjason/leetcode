class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if timeSeries==[]:
            return 0
        t=0
        timepoisoned=0
        for i in range(0,len(timeSeries)):
            
            if i==0:
                t=timeSeries[i]
            
            
            elif (timeSeries[i]-t)>=duration:
                timepoisoned=timepoisoned+duration
                
            
                t=timeSeries[i]
            else:
                timepoisoned=timepoisoned+(timeSeries[i]-t)
                t=timeSeries[i]
                
        
        timepoisoned=timepoisoned+duration
        
        return(timepoisoned)
            
