-- Retrieve each score and assign a dense rank based on descending order of scores
-- DENSE_RANK() ensures that scores with the same value share the same rank,
-- and the next distinct score gets the immediate next rank (no gaps in ranking).

SELECT 
    score, 
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM 
    Scores;
