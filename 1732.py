class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        point=0
        maxx=0
        for i in gain:
            point=point+i
            if point>maxx:
                maxx=point
        return maxx
