-- Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on my MySQL server.
-- Query that creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Query that creates the table states.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
