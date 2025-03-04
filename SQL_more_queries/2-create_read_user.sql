-- Script that creates the database hbtn_0d_2 and the user user_0d_2.
-- Query that creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Query that creates user_0d_2 with password set to user_0d_2_pwd.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Query that set only SELECT privilege in the database hbtn_0d_2 for user_0d_2. 
GRANT SELECT ON *.* TO 'user_0d_1'@'localhost';
