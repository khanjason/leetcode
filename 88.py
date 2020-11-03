class Solution:
    def mergesort(self,arr):
        if len(arr)>1:
            mid=(len(arr)//2)
            left=arr[:mid]
            right=arr[mid:]
            self.mergesort(left)
            self.mergesort(right)
            i=j=k=0
            while i<len(left) and j<len(right):
                if(left[i]) <(right[j]):
                    arr[k]=left[i]
                    i=i+1
                else:
                    arr[k]=right[j]
                    j=j+1
                k=k+1
            while i<len(left):
                arr[k]=left[i]
                i=i+1
                k=k+1
            while j < len(right):
                arr[k]=right[j]
                j=j+1
                k=k+1
            return arr
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0,len(nums2)):
            
            nums1[len(nums1)-1-i]=nums2[i]
        self.mergesort(nums1)
        
