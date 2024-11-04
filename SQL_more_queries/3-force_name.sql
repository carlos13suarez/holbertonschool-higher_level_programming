-- create the table force_name with an id column and a name column that cannot be NULL, and ensure the script does not fail if the table already exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
