
# Write an SQL query to find employees who have the highest salary in each of the departments.
with max_salary as ( select max(e.salary) as maxSalary, e.departmentId
from Employee as e
group by e.departmentID)

select d.name as Department, e.name as Employee, e.salary as Salary
from Employee as e
inner join Department as d on e.departmentId = d.id
inner join max_salary as ms on ms.maxSalary = e.salary and ms.departmentId = d.id