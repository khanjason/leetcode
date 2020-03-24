class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        namlist=[]
        counts=[]
        typelist=[]
        typecount=[]
        comp=[]
        
        c=1
        for i in name:
            
            if namlist==[]:
                namlist.append(i)
            
            elif i!=namlist[-1]:
                counts.append(c)
                namlist.append(i)
                c=1
            else:
                c=c+1
        counts.append(c)
        
        c2=1
        sw=0
        
        for t in range(0,len(typed)):
            if typelist==[]:
                typelist.append(typed[t])
                comp.append(typed[t])
                
            elif typed[t]!=typelist[-1]:
                sw=sw+1
                comp.append(typed[t])
                typecount.append(c2)
                c2=1
                typelist.append(typed[t])
                
                
                    
            else:
                c2=c2+1
                
        
        if len(comp)!=len(namlist):
            return False
        
        for ti in range(0,len(typecount)):
            if typecount[ti]< counts[ti]:
                return False
        return True
