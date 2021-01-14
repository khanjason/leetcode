class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        #x row is customer
        #j is bank
        moneys=[]
        for t in accounts:
            moneys.append(sum(t))
        return max(moneys)
