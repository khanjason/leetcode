class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tot=""
        words=[]
        if s=="":
            return 0
        for f in s:
            if f == ' ':
                if tot!= '':
                    words.append(tot)
                tot=""
            else:
                tot=tot+f
        if tot!='':
            words.append(tot)
        print(words)
        if words==[]:
            return 0
        return len(words[-1])
