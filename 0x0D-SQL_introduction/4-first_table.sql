-- script that creates a table called first_table in the current database
-- If the table first_table already exists, script not fail
-- database is pased as arguments
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
	name VARCHAR(256)
);
