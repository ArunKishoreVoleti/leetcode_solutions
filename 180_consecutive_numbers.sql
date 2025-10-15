-- Find numbers that appear in at least 3 consecutive entries in the 'logs' table

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
