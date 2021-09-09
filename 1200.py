class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr=sorted(arr)
        minabs=max(arr)
        ans=[]
        prev=arr[0]
        for t in range(1,len(arr)):
            if arr[t]-prev < minabs:
                minabs=abs(arr[t]-prev)
            prev=arr[t]
        prev=arr[0]
        for t in range(1,len(arr)):
            if arr[t]-prev == minabs:
                ans.append([prev,arr[t]])
            prev=arr[t]
        print(minabs)
        return ans
        