# Write your MySQL query statement below

# 使用join进行连接
# 连接条件是 日期相差1，且第二天温度大于第一天温度

select w1.id AS 'Id'
from weather w1 join weather w2
on datediff(w1.recordDate, w2.recordDate) = 1
and w1.Temperature > w2.Temperature