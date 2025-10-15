-- Retrieve numbers that appear at least 3 times consecutively in the 'logs' table
-- The ROW_NUMBER() function is used to assign a sequential number within each num partition
-- Subtracting this row number from the id creates a constant "group" value for consecutive occurrences
-- GROUP BY the group and num allows counting consecutive occurrences
-- HAVING COUNT(num) >= 3 ensures only numbers with at least 3 consecutive occurrences are returned

SELECT DISTINCT num AS ConsecutiveNums
FROM (
    -- Assign a "group" number to consecutive sequences of the same num
    SELECT 
        num,
        id - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS grp
    FROM logs
) t
GROUP BY grp, num
HAVING COUNT(num) >= 3;  -- Only keep groups with 3 or more consecutive occurrences
