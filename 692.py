import heapq, collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count={}
        w=[]
        heap=[]
        for word in words:
            if word not in w:
                w.append(word)
                count[word]=1
            else:
                count[word]+=1
        for w,c in count.items():
            heap.append((-c,w))
        heapq.heapify(heap)
        ans=[]
        for i in range(k):
            tmp=heapq.heappop(heap)[1]
            ans.append(tmp)
        return ans
