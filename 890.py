class Solution:
    
    def getnums(self,s):
        a=[]
        st=[]
        c=-1
        perm=''
        for i in s:
            
            if i not in a:
                c=c+1
                a.append(i)
                st.append(c)
                perm=perm+str(c)
            else:
                ind=a.index(i)
                perm=perm+str(st[ind])
        return perm
                
                
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=[]
        for thing in words:
            if(self.getnums(thing))==(self.getnums(pattern)):
                ans.append(thing)
        return ans
