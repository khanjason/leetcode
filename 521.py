class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        uncom=-1
        res = [a[i: j] for i in range(len(a)) 
          for j in range(i + 1, len(a) + 1)] 
        for st in res:
            if st not in b:
                if len(st)>(uncom):
                    uncom=len(st)
        res2 = [b[i: j] for i in range(len(b)) 
          for j in range(i + 1, len(b) + 1)] 
        for st in res2:
            if st not in a:
                if len(st)>(uncom):
                    uncom=len(st)
        return uncom
