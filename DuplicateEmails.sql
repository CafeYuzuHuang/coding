# Write your MySQL query statement below
# 2021.03.24

# Using common table expression (CTE):
# WITH cte1 AS (SELECT Email AS e, COUNT(Email) AS n FROM Person GROUP BY Email)
# SELECT cte1.e AS Email FROM cte1 WHERE cte1.n > 1
# Runtime: 291 ms (76%)

# Comparative solution: use HAVING clause
SELECT Email FROM Person GROUP BY Email HAVING Count(Email) > 1
# Runtime: 297 ms (70%)
