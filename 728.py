class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        run=[]
        inp=[]
        r=True
        for thing in range(left,right+1):
            inp.append(thing)
        for item in inp:
            for t in str(item):
                if int(t)==0:
                    r=False
                    break
                elif (item % int(t)==0):
                    r=True
                else:
                    r=False
                    break
            if r==True:
                run.append(item)
        return(run)
