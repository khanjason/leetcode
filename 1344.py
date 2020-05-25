class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #each hour= 30
        #minute= 6
        #hours to minute
        #hour * 6
        if hour==12:
            hoursdeg=(12-hour)*30+(minutes*0.5)
            mins=minutes*6
        else:
            hoursdeg=(hour*30)
            hoursdeg=hoursdeg+(minutes*0.5)
            mins=minutes*6
        diff=max(hoursdeg,mins)-min(hoursdeg,mins)
        return min(diff,360-diff)
