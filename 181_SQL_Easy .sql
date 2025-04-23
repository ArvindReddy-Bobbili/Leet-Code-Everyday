# Write your MySQL query statement below
SELECT e.name as Employee
From employee e
Inner Join Employee m
ON e.managerId = m.id
Where e.salary > m.salary
