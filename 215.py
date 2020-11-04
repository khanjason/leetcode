import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for n in nums:
            heap.append(-n)
        heapq.heapify(heap)
        t=0
        for j in range(0,k):
            t=heapq.heappop(heap)
        return -t
