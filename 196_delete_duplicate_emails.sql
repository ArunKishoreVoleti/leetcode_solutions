-- Remove duplicate records from the 'Person' table, keeping only the first occurrence (lowest id) for each email
-- Step 1: For each unique email, find the smallest id using MIN(id)
-- Step 2: Use a subquery to collect these minimum ids
-- Step 3: Delete all rows from 'Person' where id is not in the list of minimum ids
-- This ensures that only one record per email (the earliest one) remains in the table

DELETE FROM
    Person
WHERE
    id NOT IN (
        SELECT
            min_id
        FROM (
            SELECT
                MIN(id) AS min_id
            FROM
                Person
            GROUP BY
                email
        ) AS T
    );
