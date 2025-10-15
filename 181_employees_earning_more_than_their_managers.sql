-- Find employees whose salary is greater than their manager's salary

SELECT 
    e.name AS Employee
FROM 
    employee e
JOIN 
    employee m
    ON e.managerid = m.id   -- Join employee with their manager
WHERE 
    e.salary > m.salary;    -- Only keep employees earning more than their manager
