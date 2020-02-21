
class Solution:
   
    
    
    def stotarry(self,st):
        arr=[]
        for t in st:
            arr.append(t)
        return arr
    def maximum69Number (self, num: int) -> int:
        s=''
        flist=[]
        scores=[]
        for i in range(0,len(str(num))):
            stnum=self.stotarry(str(num))
            if '6' not in stnum:
                return num
            if stnum[i] =='6':
                stnum[i]='9'
            else:
                stnum[i]='6'
            flist.append(stnum)
        
        
        maxi=max(flist)
        stri=''
        
        
        return(stri.join(maxi))
        
