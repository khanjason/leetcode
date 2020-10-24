class Solution:
    def minOperations(self, logs: List[str]) -> int:
        fold=0
        for l in logs:
            if l=="../":
                if fold!=0:
                    fold=fold-1
            elif l=="./":
                fold=fold
            else:
                fold=fold+1
        return fold
