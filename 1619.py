class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr=sorted(arr)
        five=int(len(arr)*0.05)
        arr=arr[five:]
        arr=arr[:len(arr)-five]
        print(arr)
        return sum(arr)/len(arr)
