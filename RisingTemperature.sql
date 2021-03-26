# Write your MySQL query statement below
# 2021.03.26
# Note date may be in any order, thus use LAG ... OVER ... is not a good idea

# WITH hotday AS (
#     SELECT id, Temperature AS T1, LAG(Temperature, 1) OVER(ORDER BY recordDate) AS # T0 FROM weather
# )
# SELECT id FROM hotday WHERE hotday.T1 > hotday.T0

# 1st solution: 447 ms (43%)
SELECT w1.id AS Id FROM weather AS w1 INNER JOIN weather AS w0 ON DATEDIFF(w1.recordDate, w0.recordDate) = 1 AND w1.Temperature > w0.Temperature



