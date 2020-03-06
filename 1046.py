class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st=sorted(stones)
        print(st)
        while len(st)>1:
            x=st.pop()
            y=st.pop()
            if x!=y:
                n=y-x
                st.append(abs(n))
                st=sorted(st)
           
        if len(st)==1:
            return st[0]
        else:
            return 0
