class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stax=[]
        outt=[]
        for i in range(1,n+1):
            if stax==target:
                break
            
            elif i in target:
                outt.append("Push")
                stax.append(i)
            else:
                outt.append("Push")
                outt.append("Pop")
                
        return outt
