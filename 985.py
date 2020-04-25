class Solution:
    def sumeven(self,A):
        s=0
        
        for i in A:
            if i %2==0:
                s=s+i
        return s
    
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        #0th -- valie
        #1 is the ind
        #add to A
        answer=[]
        saum=self.sumeven(A)
        for query in range(0,len(queries)):
            
            if (A[queries[query][1]]) % 2==0:
                saum=saum- (A[queries[query][1]])
            (A[queries[query][1]])= (A[queries[query][1]]) + +queries[query][0]
            if (A[queries[query][1]]) % 2==0:
                saum=saum+ (A[queries[query][1]])
            answer.append(saum)
        return answer
           
