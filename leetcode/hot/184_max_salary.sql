# 部门工资最高的员工
# 先按照部门进行分组，选出部门中工资最高的员工
# 然后再进行连接操作


# Write your MySQL query statement below

select Department.NAME AS Department, Employee.NAME AS Employee, Salary
from Employee, Department
where Employee.DepartmentId = Department.Id
and (Employee.DepartmentId, Salary)
in (
    select DepartmentId, max(Salary)
    from Employee
    group by DepartmentId
)







