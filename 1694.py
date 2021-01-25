class Solution:
    def makeoutput(self,blocks):
        s=''
        
        for b in range(len(blocks)):
            for n in blocks[b]:
                s=s+n
            if b!=len(blocks)-1 and len(blocks)!=1:
                s=s+'-'
        return s
    
    
    def reformatNumber(self, number: str) -> str:
        number=number.split(' ')
        number=''.join(number)
        number=number.split('-')
        number=''.join(number)
        print(number)
        remain=len(number)%3==0
        remainder=len(number)%3
        if remainder==1:
            remainder=4
        blocks=[]
        tmp=[]
        count=0
        tot=-1
        
        for i in number:
            tot+=1
            if (len(number)-tot)==remainder and remain==False:
                break
            if count==3:
                blocks.append(tmp)
                tmp=[]
                count=0
            tmp.append(i)
            count+=1
        blocks.append(tmp)
        
        if remain:
            return self.makeoutput(blocks)
        last4=number[len(number)-remainder:]
        
        if len(last4)==4:
            count=0
            t=[]
            for y in last4:
                if count==2:
                    blocks.append(t)
                    t=[]
                    count=0
                count+=1
                t.append(y)
            blocks.append(t)
        else:
            t=[]
            for x in last4:
                t.append(x)
            blocks.append(t)
        newblocks=[]
        for item in blocks:
            if item!=[]:
                newblocks.append(item)
        return self.makeoutput(newblocks)
