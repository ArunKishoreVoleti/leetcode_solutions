-- Create a function to get the Nth highest salary from the Employee table
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    -- Since LIMIT is zero-based, we subtract 1 to align N with the OFFSET index
    SET N = N - 1;

    -- Select the distinct salary values in descending order,
    -- then skip the first (N) salaries using OFFSET, and return the next one
    RETURN (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
    );
END;
