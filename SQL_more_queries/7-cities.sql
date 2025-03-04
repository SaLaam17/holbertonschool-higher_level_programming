-- Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- Query that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Query that creates table cities (in the database hbtn_0d_usa).
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT AUTO_INCREMENT PRIMARY KEY, state_id INT FOREIGN KEY, name VARCHAR(256) NOT NULL);
