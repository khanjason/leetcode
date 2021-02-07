class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split('.')
        v2=version2.split('.')
        for t in range(0,min(len(v1),len(v2))):
            if int(v1[t])>int(v2[t]):
                return(1)
            if int(v2[t])>int(v1[t]):
                return(-1)
        
        if len(v1)>len(v2) and int(''.join(v1[len(v2):]))!=0:
            return 1
        if len(v2)>len(v1) and int(''.join(v2[len(v1):]))!=0:
            return -1
        return 0
