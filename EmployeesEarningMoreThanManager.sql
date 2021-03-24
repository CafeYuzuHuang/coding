# Write your MySQL query statement below
# 2021.03.24

# Using self-query
SELECT e1.Name AS Employee FROM Employee AS e1, Employee AS e2 WHERE e1.ManagerId = e2.Id AND e1.Salary > e2.Salary
