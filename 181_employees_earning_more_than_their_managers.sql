-- Retrieve employees whose salary is greater than their manager's salary
-- A self-join is used to link each employee to their manager using managerid
-- The WHERE clause filters only employees earning more than their manager

SELECT 
    e.name AS Employee
FROM 
    employee e
JOIN 
    employee m
    ON e.managerid = m.id   -- Link employee to their manager
WHERE 
    e.salary > m.salary;    -- Keep only employees with salary greater than their manager
