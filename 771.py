class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        #together=J+S
        C=0
        both=[]
        for item in S:
            if item in J:
                if item not in both:
                    both.append(item)
        for i in both:
            C=C+(S.count(i))
        return(C)
