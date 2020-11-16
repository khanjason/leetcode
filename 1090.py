from itertools import *
class Solution:
    
      
    # function to generate all the sub lists 
    
    
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        d={}
        m=0
        li=[]
        for i in range(len(values)):
            li.append((values[i],labels[i]))
        
        li=sorted(li, key= lambda x: x[0], reverse=True)
        for v,l in li:
            if num_wanted==0:
                break
            if l in d.keys():
                if d[l]<use_limit:
                    m=m+v
                    d[l]=d[l]+1
                    num_wanted=num_wanted-1
            else:
                m=m+v
                d[l]=1
                num_wanted=num_wanted-1
                
            
                
        return m
