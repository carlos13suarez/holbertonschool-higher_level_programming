-- create the table id_not_null with an id column that has a default value of 1 and a name column, and to ensure the script does not fail if the table already exists
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
