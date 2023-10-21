-- script that lists the number of records with the same score in second_table
-- The result should display: the score, the number of records
-- that is; The result should display:
-- the score
-- the number of records for this score with the label number
SELECT score, COUNT(score) AS "number" FROM second_table GROUP BY score ORDER BY score DESC;
