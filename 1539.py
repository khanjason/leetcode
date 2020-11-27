class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        heap=[]
        heapq.heapify(heap)
        c=0
        while len(heap)<k:
            c=c+1
            if c not in arr:
                heapq.heappush(heap,c)
        for t in range(k):
            a= heapq.heappop(heap)
        return a
