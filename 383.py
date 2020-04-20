class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        used=[]
        counts=[]
        for i in ransomNote:
            c=0
            if i not in magazine:
                return False
            else:
                if i not in used:
                    used.append(i)
                    counts.append(c+1)
                else:
                    ind=used.index(i)
                    counts[ind]=counts[ind]+1
                    if counts[ind]>magazine.count(i):
                        return False
        return True
