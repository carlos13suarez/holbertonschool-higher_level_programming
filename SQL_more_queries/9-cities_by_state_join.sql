-- list all cities in the database hbtn_0d_usa by displaying id, name and its states name, sorting the id in ascending order
SELECT cities.id, cities.name, (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
