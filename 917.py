class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        lets=[]
        outt=''
        alp='abcdefghijklmnopqrstuvwxyz'
        for x in S:
            if x.lower() in alp:
                lets.append(x)
        c=0
        for thing in S:
            if thing.lower() not in alp:
                outt=outt+thing
            else:
                num=c+1
                outt=outt+lets[-num]
                c=c+1
        return(outt)
