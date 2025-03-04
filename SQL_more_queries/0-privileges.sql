-- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on my server (in localhost).
-- Query that creates user_0d_1
CREATE USER 'user_0d_1'@'localhost';
-- Query that creates user_0d_2
CREATE USER 'user_0d_2'@'localhost';
-- Query that lists all privileges of the MySQL users user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- Query that lists all privileges of the MySQL users user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
