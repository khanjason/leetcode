class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        print(flowerbed)
        nex=True
        c=0
        for thing in flowerbed:
            if thing==1:
                if nex==False:
                    c=c-1
                nex=False
            if thing==0:
                if nex==True:
                    c=c+1
                    nex=False
                else:
                    nex=True
        if c>=n:
            return True
        else:
            return False
