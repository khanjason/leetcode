
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        
        for i in set(nums):
            freq[i]=nums.count(i)
            
        
        li=heapq.nlargest(k,freq.keys(),key=freq.get)
        
        return li
        
