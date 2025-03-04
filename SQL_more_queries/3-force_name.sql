-- Script that creates the table force_name on my MySQL server.
-- Query that creates the table force_name.
-- If the table force_name already exists, the script should not fail.
-- force_name description: id INT name VARCHAR(256) can’t be null.
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);

