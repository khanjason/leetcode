class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #find dest
        start=paths[0]
        for i in range(0,len(paths)):
            for j in range(0,len(paths)):
                if start[1]==paths[j][0]:
                    start=paths[j]
        return start[1]
                    
                
