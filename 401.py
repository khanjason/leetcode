from itertools import combinations, permutations, combinations_with_replacement 
class Solution:
    def sortsol(self,arr):
        n=[]
        for thing in arr:
            thing=thing.replace(':','.')
            
            t=float(thing)
            n.append(t)
        
        new=(sorted(n))
        for item in range(0,len(new)):
            nstring=str(new[item])
            nstring=nstring.replace('.',':')
            if len(nstring[nstring.index(':'):])==2:
                nstring=nstring+'0'
            new[item]=nstring
        return new
    
    def getcombs(self,arr,n):
        li=[]
        lst = map(list,(itertools.product([0, 1], repeat=10)))
        for t in lst:
            if t.count(1)==n:
                li.append(t)
        return(li)
    
    
    def coverttotime(self,cl):
        tot1=0
        tot2=0
        for thing in range(0,len(cl)):
            
            if cl[thing]==1:
                
                if thing<4:
                    
                    tot1=tot1+(2**thing)
       
                
                if thing>=4:
                    
                    tot2=tot2+(2**(thing-4))
        
        return tot1,tot2
    def readBinaryWatch(self, num: int) -> List[str]:
        if num==0:
            return ["0:00"]
        finl=[]
        clock=[0,0,0,0,0,0,0,0,0,0]
        ind=0
        for item in range(0,num):
            clock[item]=1
            
        
        lioli=self.getcombs(clock,num)
        for thi in lioli:
            hour=0
            mint=0
            hour,mint=(self.coverttotime(thi))
            m=mint
            if len(str(mint))==1:
                mint='0'+str(mint)
            if (hour>=12) or (m>=60):
                print()
            else:
                finl.append(str(hour)+':'+str(mint))
        finl=self.sortsol(finl)
        return finl
        
