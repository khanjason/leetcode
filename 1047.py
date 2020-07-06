class Solution:
    def removeDuplicates(self, S: str) -> str:
        arr=['']
        for i in S:
            if i!=arr[-1]:
                arr.append(i)
            else:
                arr.pop()
                continue
        
            
        return ''.join(arr)
