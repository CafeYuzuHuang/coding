# Write your MySQL query statement below

# 2021.03.24
# SELECT p.FirstName, p.LastName, a.City, a.State FROM Person AS p, Address as a WHERE p.PersonId = a.PersonId # wrong answer

# Use LEFT JOIN to guerantee person full name will be shown regardless the query results.
SELECT p.FirstName, p.LastName, a.City, a.State FROM Person AS p LEFT OUTER JOIN Address as a ON p.PersonId = a.PersonId


