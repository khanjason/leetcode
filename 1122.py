class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        end=[]
        for i in arr1:
            if i not in arr2:
                end.append(i)
        end=sorted(end)

        test=[]
        for n in arr2:
            for t in range(0,arr1.count(n)):
                test.append(n)
        return test+end
                
            
