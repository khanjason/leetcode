class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        heapq.heapify(heap)
        for i in matrix:
            for j in i:
                heapq.heappush(heap,j)
                
        for t in range(k):
            a=heapq.heappop(heap)
        return a
