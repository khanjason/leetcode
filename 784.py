from itertools import product
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        li1=[]
        
        a=[]
        
        nums=['0','1','2','3','4','5','6','7','8','9']
        for thing in S:
            if thing not in nums:
                li1.append(thing.upper())
                
        
        perm=product(['u','l'],repeat=len(li1)) 
        for i in list(perm):
            st=''
            c=-1
            for t in S:
                if t not in nums:
                    c=c+1
                    if i[c]=='u':
                        st=st+(t.upper())
                    if i[c]=='l':
                        st=st+(t.lower())
                else:
                    st=st+t
            a.append(st)
        return(a)
