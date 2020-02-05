from itertools import product
class Solution:
    def binaries(self,lower,upper):
        st=(0,0)
        li=[st]
        while st[0]!=upper and st[1]!= upper:
            st=(st[0],st[1]+1)
            li.append(st)
            st=(st[0]+1,st[1])
            li.append(st)
            
        return li
    
    
    def method(self,x,y,bound):
        li=[]
        fin=[]
        for i in range(0,22):
            li.append(i)
        prod= product(li,repeat=2)
        
        for thing in list(prod):
            
            
            if (x**(thing[0]) +y**(thing[1]))<=bound:
                
                    ans=((x**(thing[0]) +y**(thing[1])))
                    if ans not in fin:
                        fin.append(ans)
            
        return fin
    
    
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        return sorted(self.method(x,y,bound))
