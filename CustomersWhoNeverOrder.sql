# Write your MySQL query statement below
# 2021.03.24

# Use NOT IN subquery and INNER JOIN clause
# SELECT Name AS Customers FROM Customers WHERE Id NOT IN (SELECT c.Id FROM Customers AS c INNER JOIN Orders AS o ON c.Id = o.CustomerId)
# Runtime: 447 ms (53%)

# 2nd approach: INNER JOIN is uncessary!
SELECT Name as Customers FROM Customers WHERE Id NOT IN (SELECT CustomerId  FROM Orders)
# Runtime 435 ms (61%)
