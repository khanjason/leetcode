class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurs=[]
        ran=[]
        for each in arr:
            if each not in ran:
                occurs.append(arr.count(each))
                ran.append(each)
        print(occurs)
        count=0
        for item in occurs:
            if occurs.count(item)==1:
                count=count+1
        if count==len(occurs):
            return True
        else:
            return False
