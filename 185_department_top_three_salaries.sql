-- Retrieve the highest-paid employee(s) in each department
-- Use DENSE_RANK() to assign ranks to employees within each department based on descending salary
-- Employees with the highest salary (rank < 4) are selected as top 3 highest-paid employees per department

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
    rnk < 4 -- Keep only top 3 highest-paid employees per department
