class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        copy=[]
        for n in code:
            copy.append(n)
        if k>0:
            for item in range(len(code)):
                if len(code)-item>abs(k):
                    
                    code[item]=sum(copy[item+1:item+abs(k)+1])
                else:
                    m=k-(len(code)-item)
                
                    s=sum(copy[item+1:])
                    t=sum(copy[:m+1])
                    code[item]=t+s
        elif k<0:
            for item in range(len(code)):
                if item>=abs(k):
                    code[item]=sum(copy[item-abs(k):item])
                else:
                    m=item-abs(k)
                    
                    s=sum(copy[:item])
                    t=sum(copy[len(code)-abs(m):])
                    code[item]=t+s
        else:
            for item in range(len(code)):
                code[item]=0
        return code
