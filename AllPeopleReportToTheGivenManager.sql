SELECT employee_id
FROM Employees
WHERE manager_id IN (
		SELECT employees.employee_id
		FROM Employees AS employees
		INNER JOIN Employees AS managers ON employees.manager_id = managers.employee_id
		/*exclude boss, exclude directly reporting to boss, exclude manager that do not report boss*/
		WHERE employees.manager_id = 1
			OR (
				employees.employee_id <> employees.manager_id
				AND managers.manager_id = 1
				)
		)
	AND employee_id <> manager_id
