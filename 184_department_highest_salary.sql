-- Retrieve the highest-paid employee(s) in each department
-- Use DENSE_RANK() to assign ranks to employees within each department based on descending salary
-- Employees with the highest salary (rank = 1) are selected as top earners per department

SELECT 
    department, 
    employee, 
    salary
FROM (
    SELECT 
        d.name AS Department, 
        e.name AS Employee, 
        e.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS rnk
    FROM 
        department d
    INNER JOIN 
        employee e
    ON 
        d.id = e.departmentId
) ranked_employees
WHERE 
    rnk = 1;  -- Keep only top-ranked (highest-paid) employees per department
