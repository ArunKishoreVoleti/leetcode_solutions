/*
This query returns the second highest salary from the Employee table.
If there is no second highest salary, it returns NULL.
It uses COUNT(DISTINCT Employee.salary) to check if there are at least two unique salaries.
If so, it selects the MAX(Employee.salary) after excluding the highest salary.
*/

SELECT
    CASE
        WHEN COUNT(DISTINCT Employee.salary) < 1 THEN NULL
        ELSE MAX(Employee.salary)
    END AS SecondHighestSalary
FROM Employee
WHERE Employee.salary < (
    SELECT MAX(salary)
    FROM Employee
);