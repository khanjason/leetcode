class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid=int(len(s)/2)
        first=s[:mid]
        second=s[mid:]
        vows='aeiou'
        count1=0
        for i in first:
            if i.lower() in vows:
                count1+=1
        count2=0
        for t in second:
            if t.lower() in vows:
                count2+=1
        return count1==count2
