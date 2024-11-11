-- list all cities in the database hbtn_0d_usa by displaying id, name and its
-- states name, sorting the id in ascending order
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
