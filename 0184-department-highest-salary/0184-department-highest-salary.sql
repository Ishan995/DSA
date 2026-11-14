# Write your MySQL query statement below
SELECT d.name AS Department,
e.name AS Employee,
e.salary AS Salary
FROM Employee e
inner join department d
on e.departmentID=d.id 
where e.salary=(
    select max(e2.salary)
    from employee e2
    where e.departmentId=e2.departmentId)