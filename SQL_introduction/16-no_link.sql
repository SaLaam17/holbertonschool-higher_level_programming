-- Script that lists all records of the table second_table of the database hbtn_0c_0 in my MySQL server.
-- Query display the score the number of records for this score with the label number.
-- The list should be sorted by the number of records (descending).
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
