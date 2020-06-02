class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        Ac=''
        Bc=''
        for i in range(0,len(a)):
            if a[i]=='+':
                Bc=a[i+1:]
                break
            else:
                Ac=Ac+a[i]
        print(Ac,Bc)
        Ad=''
        Bd=''
        for i in range(0,len(b)):
            if b[i]=='+':
                Bd=b[i+1:]
                break
            else:
                Ad=Ad+b[i]
        print(Ad,Bd)
        first=int(Ac)*int(Ad)
        second=int(Bc[:len(Bc)-1])*int(Ad)
        third=int(Bc[:len(Bc)-1])*int(Bd[:len(Bd)-1])
        four=int(Ac)*int(Bd[:len(Bd)-1])
        tot1=first-(third)
        tot2=second+four
        totfin=str(tot1)+'+'+str(tot2)+'i'
        return totfin
