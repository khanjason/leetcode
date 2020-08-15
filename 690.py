"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getdfs(self,target,emap):
        employee = emap[target]
        return (employee.importance +sum(self.getdfs(target,emap) for target in employee.subordinates))
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}
        return self.getdfs(id,emap)
