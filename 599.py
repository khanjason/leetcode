class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        output=[]
        scores=[]
        for i in range(0,len(list1)):
            if list1[i] in list2:
                output.append(list1[i])
                score=i+list2.index(list1[i])
                scores.append(score)
        if scores.count(min(scores))>1:
            return output
        ind=scores.index(min(scores))
        return([(output[ind])])
