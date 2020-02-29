class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        li=[]
        for item in A:
            li.append(pow(item,2))
        return sorted(li)
