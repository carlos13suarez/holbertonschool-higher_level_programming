-- list all Comedy shows in the hbtn_0d_tvshows database
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy')
ORDER BY tv_shows.title ASC;
