# Write your MySQL query statement below

# 2021.03.24
# Note: 
# (1) Change the column name via AS [new_col_name]
# (2) Use DISTINCT keyword to exclude duplicates
# (3) Use IFNULL function to present NULL rather than empty
SELECT IFNULL( (SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary ; # runtime 74%



