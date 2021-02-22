class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        b=[]
        for bi in boxes:
            b.append(bi)
        boxes=b
        
        ans=[]
        for i in range(0,len(boxes)):
            c=0
            first=boxes[:i]
            for t in range(0,len(first)):
                if first[t]=='1':
                    c=c+(i-t)
            second=boxes[i+1:]
            
            for y in range(0,len(second)):
                if second[y]=='1':
                    c=c+y+1
            
            ans.append(c)
        return ans
        
