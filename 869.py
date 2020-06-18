from itertools import permutations
import math
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        nlist=[]
        for i in str(N):
            nlist.append(i)
        c=permutations(nlist,len(nlist))
        for t in c:
            if t[0]!='0':
                num=int(''.join(t))
                
                if math.log2(num).is_integer():
                    return True
        return False
            
