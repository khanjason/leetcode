class Solution:
    def totalMoney(self, n: int) -> int:
        tot=0
        r=n%7
        cut=int(n/7)
        print(cut)
        counter=0
        while cut>0:
            for i in range(1,8):
                tot+=(counter+i)
            cut-=1
            counter+=1
        for t in range(1,r+1):
            tot+=counter+t
        return tot
        
        
        return ((cut+3)*7)
        #28 # base # 4 *7
        #35 5 * 7
        #42 = 6 * 7
