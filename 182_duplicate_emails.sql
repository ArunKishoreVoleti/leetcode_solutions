-- Approach 1: Using GROUP BY and HAVING (Commented)
-- SELECT email
-- FROM person
-- GROUP BY email
-- HAVING COUNT(*) > 1;

-- Approach 2: Using ROW_NUMBER() and DISTINCT
SELECT DISTINCT email
FROM (
    -- Assign a row number to each email partitioned by email
    SELECT 
        email,
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY email) AS rn
    FROM person
) t
WHERE rn > 1;  -- Keep only rows beyond the first occurrence, i.e., duplicates
