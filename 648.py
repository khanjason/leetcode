class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        senlist=sentence.split( )
        for i in range(0,len(senlist)):
            for r in dict:
                if r in senlist[i]:
                    j=''
                    for c in senlist[i]:
                        if j==r:
                            senlist[i]=r
                            break
                        j=j+c
                    
        ans=''
        for item in range(0,len(senlist)-1):
            ans=ans+senlist[item]+' '
        ans=ans+senlist[len(senlist)-1]
        return ans
