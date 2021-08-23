class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d={}
        
        for item in edges:
            for n in item:
                if n in d.keys():
                    d[n]=d[n]+1
                else:
                    d[n]=1
        for k in d.keys():
            if d[k]==len(edges):
                return k