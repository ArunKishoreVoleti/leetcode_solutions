-- Retrieve the IDs of dates where the temperature is higher than the previous day's temperature
-- Step 1: Perform a self-join on the Weather table to compare each record with its previous day's record
-- Step 2: Use DATEDIFF() = 1 to ensure the two dates are consecutive
-- Step 3: Return the ID of the date where temperature increased compared to the previous day

SELECT 
    w1.Id
FROM 
    Weather w1
JOIN 
    Weather w2
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1  -- Consecutive days
WHERE 
    w1.temperature > w2.temperature;  -- Temperature higher than the previous day

-- Retrieve IDs where the temperature is higher than the previous day using LAG()
-- Step 1: Use LAG() to access the previous record’s temperature and date
-- Step 2: Ensure dates are consecutive (DATEDIFF = 1)
-- Step 3: Keep records where current temperature > previous temperature

-- SELECT 
--     id
-- FROM (
--     SELECT 
--         id,
--         recordDate,
--         temperature,
--         LAG(recordDate) OVER (ORDER BY recordDate) AS prevDate,
--         LAG(temperature) OVER (ORDER BY recordDate) AS prevTemp
--     FROM 
--         Weather
-- ) t
-- WHERE 
--     DATEDIFF(recordDate, prevDate) = 1  -- consecutive days
--     AND temperature > prevTemp;          -- temperature increased
