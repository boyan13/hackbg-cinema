ADD_MOVIE = '''
INSERT INTO MOVIES (name, rating)
VALUES (?, ?);
'''

SHOW_MOVIES = '''
SELECT * FROM MOVIES ORDER BY rating DESC;'''

GET_MOVIE_BY_ID = '''
SELECT *
FROM Movies
WHERE id = ?;'''

