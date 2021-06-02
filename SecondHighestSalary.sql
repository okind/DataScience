select (
    select
        distinct e.Salary
    from
        Employee e
    order by
        e.Salary desc
    offset
        1 ROWS
    fetch
        NEXT 1 ROWS ONLY) as SecondHighestSalary
