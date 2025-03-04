-- Script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in my MySQL server.
-- Query that displays both the score and the name (in this order) ordered by score (top first)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
