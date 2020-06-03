class Solution:
    def tobin(self,n):
        st=''
        while n>1:
            if n%2==0:
                st.append('0')
            else:
                st.append('1')
            n=int(n/2)
        return st[::-1]
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
      
            
        rang=[]
        tot=0
        for i in range(0, len(arr)):
            tot=tot^arr[i]
            rang.append(tot)
        
        res=[]
        for q in queries:
            s,e = q
            if s!=e:
                if s>0:
                    t0 = rang[e]
                    t1 = rang[s-1]
                    t = t0 ^ t1
                else:
                    t = rang[e]
            else:
                t = arr[s]
            res.append(t)
        return res
