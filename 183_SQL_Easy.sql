# Write your MySQL query statement below
Select name as Customers
From Customers as c
left join Orders as o
on c.id = o.customerId
Where customerId is NULL