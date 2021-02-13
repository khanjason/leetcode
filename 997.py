class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        #trust[0] trusts trust[1]
        if N==1:
            return 1
        people=[]
        for i in range(1,N+1):
            people.append(i)
        d={}
        for t in trust:
            if t[0] not in d.keys():
                d[t[0]]=[t[1]]
            else:
                d[t[0]].append(t[1])
        if trust==[]:
            return -1
        
        
        if len(d.keys())!=len(people)-1:
            return -1
        for p in people:
            caught=False
            if p not in d.keys():
                
                for k,v in d.items():
                    if p not in v:
                        caught=True
                        
                        break
                if caught==False:
                    return p
        return -1
