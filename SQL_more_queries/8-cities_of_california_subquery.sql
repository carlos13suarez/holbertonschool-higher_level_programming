-- list all the cities of California in the database hbtn_0d_usa without using the JOIN keyword
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
