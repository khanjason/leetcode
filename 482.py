class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        li=[]
        strr=""
        for i in S:
            if i!='-':
                strr=strr+(i.upper())
        REVstrr=strr[::-1]
        
        c=1
        mini=''
        for t in REVstrr:
            if (c% K==0):
                mini=mini+t
                li.append(mini)
                mini=""
            
            else:
                mini=mini+t
            c=c+1
        if mini!="":
            li.append(mini)
        
        outstring=""
        for group in range(len(li)-1,-1,-1):
            if group==0:
                outstring=outstring+((li[group])[::-1])
            else:
                outstring=outstring+((li[group])[::-1])+"-"
        return(outstring)
            
