-- list all shows in the hbtn_0d_tvshows database that have at least one genre linked, displaying each show's title and the genre ID
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
