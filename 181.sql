# Write your MySQL query statement below
SELECT e.Name as Employee
FROM Employee e, Employee m
WHERE m.Id = e.ManagerId and e.Salary > m.Salary
