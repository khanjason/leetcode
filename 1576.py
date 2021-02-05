class Solution:
    def modifyString(self, s: str) -> str:
        alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','w','x','y','z']
        st=''
        
        if len(s)<2:
            if s[0]=='?':
                return 'a'
            else:
                return s
        
        for i in range(0,len(s)):
            
            if s[i]=='?':
                for a in alp:
                    if i==0:
                        if a!=s[i+1]:
                            st=st+a
                            break
                    elif i==len(s)-1:
                        if a!=s[i-1] and a!=st[i-1]:
                            st=st+a
                            break
                        
                    else:
                    
                        if a!=s[i-1] and a!=s[i+1] and a!=st[i-1]:
                            st=st+a
                            break
            else:
                st=st+s[i]
        return st
