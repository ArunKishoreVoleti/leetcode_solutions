-- Approach 1: Using GROUP BY and HAVING (Commented)
-- Identify duplicate emails by grouping on email and selecting groups with count > 1
-- SELECT 
--     email
-- FROM 
--     person
-- GROUP BY 
--     email
-- HAVING 
--     COUNT(*) > 1;

-- Approach 2: Using ROW_NUMBER() and DISTINCT
-- Assign a row number to each email using ROW_NUMBER(), partitioned by email
-- This ranks duplicate occurrences of each email
-- Retain only rows where rn > 1, i.e., emails appearing more than once

SELECT DISTINCT email
FROM (
    SELECT 
        email,
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY email) AS rn
    FROM 
        person
) t
WHERE rn > 1;  -- Keep only duplicate email entries
