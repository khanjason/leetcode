class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        output=[]
        lis=text.split(" ")
        cat=True
        while cat:
            if (first in lis) and (second in lis) and (len(lis)>2):

                    a=(lis.index(first))
                    b=(lis.index(second))

                    if b==a+1:

                            third=lis[b+1]
                            output.append(third)
                            lis=lis[b:]
                    else:
                        lis=lis[1:]
            else:
                cat=False

        
        return(output)
        
