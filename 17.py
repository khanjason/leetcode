from itertools import product
class Solution:
    
    def prod(self,arglist,repeat=1):
        args=tuple()
        
        args=tuple(arglist)
        pools = [tuple(pool) for pool in args] * repeat
        result = [[]]
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
        for prod in result:
            yield tuple(prod)
    
    def letterCombinations(self, digits: str) -> List[str]:
        li=[]
        final=[]
        if digits=='':
            return ([])
        dictionaru= {1:'',2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        for i in digits:
            li.append(list(dictionaru[int(i)]))
        
        
        comb=self.prod(li)
        for thing in (list(comb)):
            
            s=''
            for item in thing:
                s=s+item
            final.append(s)
        return(final)
