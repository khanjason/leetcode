class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        ans=[]
        tot=0
        al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        linecount=0
        lastline=0
        for t in s:
            ind=al.index(t)
            if lastline+widths[ind] >100:
                linecount+=1
                lastline=0
            tot=tot+widths[ind]
            lastline+=widths[ind]
        linecount=linecount+1
        
        ans.append(linecount)
        ans.append(lastline)
        return ans
