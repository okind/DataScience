
--second highest salary task
SELECT
  (SELECT DISTINCT E.Salary
   FROM Employee E
   ORDER BY E.Salary DESC
   OFFSET 1 ROWS FETCH NEXT 1 ROWS ONLY) AS Secondhighestsalary
