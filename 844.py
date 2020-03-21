class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        SA=[]
        for item in S:
            SA.append(item)
        c=0
        for i in range(0,len(SA)):
            i=i-c
            if SA[i]=='#':
                if i==0:
                    del SA[i]
                    c=c+1
                else:
                    del SA[i-1]
                    c=c+1

                    del SA[i-1]
                    c=c+1
        S=''.join(SA)
        TA=[]
        for it in T:
            TA.append(it)
        count=0
        for i in range(0,len(TA)):
            i=i-count
            if TA[i]=='#':
                if i==0:
                    del TA[i]
                    count=count+1
                else:
                    del TA[i-1]
                    count=count+1
                    del TA[i-1]
                    count=count+1
        T=''.join(TA)
        if S==T:
            return True
        return False
