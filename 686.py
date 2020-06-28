class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
      
        maxx=(len(B)-1)// len(A)+1
        for i in range(0,2):
            if B in A*(maxx+i):
                return maxx+i
        return -1
