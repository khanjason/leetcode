class Solution:
    
        
    def generate(self, numRows: int) -> List[List[int]]:
        lioli=[]
        first=[1]
        second=[1,1]
        if numRows>=1:
            lioli=[first]
        gennumber=numRows
        g=1
        while g<gennumber:
            li=[1]
            i=0
            t=0
            goal=g
            for ti in range(0,g-1):
                li.append(second[i]+second[i+1])
                i=i+1
            t=t+1
            
            g=g+1
            li.append(1)
            second=li
            
            lioli.append(li)
        
        return lioli
