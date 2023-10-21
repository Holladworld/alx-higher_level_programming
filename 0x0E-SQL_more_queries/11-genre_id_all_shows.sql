-- script that lists all shows contained in the database hbtn_0d_tvshows
-- You can use only one SELECT statement
--- use join to display data and order basee on title and genre id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
