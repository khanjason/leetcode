class Solution:
    def clumsy(self, N: int) -> int:
        order=['*','//','+','-']
        c=0
        ex=''
        for i in range(N,0,-1):
            ex=ex+str(i)
            if i!=1:
                ind=c%4
                ex=ex+order[ind]
            c=c+1
        #c%4
        #print(ex)
        return (eval(ex))
