class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        tot=""
        for t in s:
            tot=tot+t
            if part in tot:
                tot=tot.replace(part,"")
        return tot
