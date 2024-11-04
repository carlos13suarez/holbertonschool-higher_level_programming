-- create the table unique_id with an id column that has a default value of 1 and must be unique, along with a name column
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
