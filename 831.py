class Solution:
    def masknumbers(self,numbers):
        symbols=['+','-','(',')',' ']
        digs=['1','2','3','4','5','6','7','8','9','0']
        newnums=''
        for i in numbers:
            if i in digs:
                newnums=newnums+i
        numbers=newnums
        
        
        
        final=[]
        local=numbers[len(numbers)-10:]
        if len(numbers)>10:
            country=numbers[:len(numbers)-10]
            c='+'
            for t in country:
                c=c+'*'
            c=c+'-'
            final.append(c)
        
        last=local[len(local)-4:]
        local=local[:len(local)-4]
        lo=''
        c=0
        for x in local:
            if x in digs:
                c=c+1
                if c==4:
                    lo=lo+'-'
                    c=0
                lo=lo+'*'
            
        final.append(lo)
        final.append('-'+last)
        return(''.join(final))
            
    
    
    def maskEmail(self,email):
        names=[]
        name1=''
        name2=''
        for i in range(0,len(email)):
            if email[i]=='@':
                email=email[i:]
                break
            else:
                name1=name1+email[i]
        name1=name1.lower()
        first=name1[0]
        last=name1[-1]
        
        name1=first+"*****"+last
        names.append(name1)
        for c in range(0,len(email)):
            if email[c]=='.':
                email=email[c:]
                break
            else:
                name2=name2+email[c]
        names.append(name2.lower())
        names.append(email.lower())
        return ''.join(names)
        
    def maskPII(self, S: str) -> str:
        if '@' in S:
            return(self.maskEmail(S))
        else:
            return (self.masknumbers(S))
