class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ss=''
        end=[]
        for thing in s:
            ss=ss+thing
            if ss.count('L')==ss.count('R'):
                end.append(ss)
                ss=''
        return(len(end))
