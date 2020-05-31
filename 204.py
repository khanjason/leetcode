class Solution:
    def countPrimes(self, n: int) -> int:
        primes=[]
        for i in range(0,n+1):
            primes.append(True)
            
        p=2
        
        while p*p<n:
            if primes[p]==True:
                for y in range(p*p,n,p):
                    primes[y]=False
            p=p+1
        
        count=0 
        for t in range(2,n):
            if primes[t]==True:
                count=count+1
        return count
        
                    
