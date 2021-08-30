class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d=[]
        a=[]
        for i in s:
            if i not in d:
                a.append(s.count(i))
                d.append(i)
        start=a[0]
        for t in a:
            if t!=start:
                return False
        return True