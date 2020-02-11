class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        together=A+' '+B
        li=[]
        for item in together.split(" "):
            
            if (together.split(" ")).count(item)==1:
                li.append(item)
        return(li)
