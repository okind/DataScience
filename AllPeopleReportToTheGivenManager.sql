SELECT Employee_id
FROM Employees
WHERE Manager_id IN
    (SELECT Employees.Employee_id
     FROM Employees AS Employees
     INNER JOIN Employees AS Managers ON Employees.Manager_id = Managers.Employee_id
     /*exclude boss, exclude directly reporting to boss, exclude manager that do not report boss*/
     WHERE Employees.Manager_id = 1
       OR (Employees.Employee_id <> Employees.Manager_id
           AND Managers.Manager_id = 1) )
  AND Employee_id <> Manager_id
