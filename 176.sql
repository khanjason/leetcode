# Write your MySQL query statement below
select
IFNULL(
(select distinct Salary as SecondHighestSalary
From Employee
order by Salary Desc
LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary


