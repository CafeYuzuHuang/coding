# Write your MySQL query statement below

# 2021.03.26
# 1st: straight forward: 2021 ms (13% ...)
# DELETE p1 FROM Person p1, Person p2 WHERE p1.Email = p2.Email AND p1.Id > p2.Id


# 2nd: Self join: 1670 ms (53%)
# DELETE p1 FROM Person p1 INNER JOIN Person p2 ON p1.Email = p2.Email AND p1.Id > p2.Id;


# 3rd: Group by: 1380 ms (90%)
# DELETE FROM Person WHERE id NOT IN (SELECT * FROM (SELECT MIN(p.Id) FROM Person p GROUP BY p.Email) AS tmp )


# 4th: Window function: 1312 ms (97% !!!)
DELETE FROM Person WHERE id NOT IN (
    SELECT * FROM (
        SELECT FIRST_VALUE(p.Id) OVER(PARTITION BY p.Email ORDER BY p.Id ASC) FROM Person p
    ) AS tmp 
)



