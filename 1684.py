class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        co=0
        for w in words:
            m=False
            for c in w:
                if c not in allowed: 
                    m=True
                    break
            if not m:
                co+=1
        return co
                
