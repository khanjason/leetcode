class Solution:
    def getlistofprimes(self,length):
        li=[]
        c=False
        for y in range(2,length+1):
            c=False
            if y==2:
                li.append(str(y))
            elif y %2==1:
                for item in li:
                    if y % int(item) ==0:
                        c=True
                        print('ok')
                        
                if c==False:
                    li.append(str(y))
        return li
                
    
    def tobin(self,i):
        st=""
        while i>0:
            if i%2==1:
                st=st+'1'
            else:
                st=st+'0'
            i=int(i/2)
        return st[::-1]
    def countPrimeSetBits(self, L: int, R: int) -> int:
        #all odds numbers up to 2^n 
        maxlen=len(self.tobin(R))
        
        counter=0
        primeli=self.getlistofprimes(maxlen)
        
        
        for t in range(L,R+1):
            
            binnum=(self.tobin(t))
            
            if (str(binnum.count('1'))) in primeli:
                counter=counter+1
        return(counter)
        
