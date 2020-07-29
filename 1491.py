class Solution:
    def average(self, salary: List[int]) -> float:
        maxx=max(salary)
        minn=min(salary)
        for i in range(0,len(salary)):
            if salary[i]==maxx or salary[i]==minn:
                salary[i]=0
        avg=sum(salary)/(len(salary)-2)
        return avg
