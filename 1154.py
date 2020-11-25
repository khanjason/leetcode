class Solution:
    def dayOfYear(self, date: str) -> int:
        #ignore the year
        #retrieve month into an int
        #map int to 31,28,31,30,31,30,31,31,30,31,30,31
        #add day
        li=date.split('-')
        mon=int(li[1])
        day=int(li[2])
        year=int(li[0])
        print(mon)
        print(day)
        d={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        msum=0
        for i in range(1,mon):
            offset=0
            if i==2:
                if year%100==0:
                    if year%400==0:
                        offset=1
                
                elif year%4==0:
                    offset=1
            msum=msum+d[i]+offset
        ans=msum+day
        return ans
