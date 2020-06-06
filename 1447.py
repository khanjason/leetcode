class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        bot=''
        top=''
        frac=[]
        done=set()
        for i in range(1,n):
            for t in range(i+1,n+1):
                if i/t in done:
                    continue
                done.add(i/t)
              
				
                frac.append(str(i)+'/'+str(t))
        return(frac)
  
