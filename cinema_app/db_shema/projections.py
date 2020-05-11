ADD_PROJECTION = '''
INSERT INTO Projections(movie_id, date, time, type)
VALUES (?, ?, ?, ?);
'''

SHOW_ALL_PROJECTIONS = '''
SELECT p.id,  p.date, p.time, p.type, 100 - COUNT(r.id)
FROM Projections AS p left JOIN Reservations AS r ON p.id = r.projection_id
WHERE movie_id = ?
GROUP BY p.id
ORDER BY date ASC;
'''

SHOW_ALL_PROJECTIONS_D = '''
SELECT p.id,  p.date, p.time, p.type, 100 - COUNT(r.id)
FROM Projections AS p left JOIN Reservations AS r ON p.id = r.projection_id
WHERE movie_id = ?
GROUP BY p.id
ORDER BY date DESC;
'''

SHOW_PROJECTIONS = '''
SELECT p.id,  p.date, p.time, p.type, 100 - COUNT(r.id)
FROM Projections AS p left JOIN Reservations AS r ON p.id = r.projection_id
WHERE movie_id = ? and date like ?
GROUP BY p.id;
'''

GET_ALL_PROJECTIONS_old = '''
SELECT m.name, p.time, p.date, p.id
FROM Projections AS p LEFT JOIN Movies AS m
ON p.movie_id = m.id
'''

GET_ALL_PROJECTIONS = '''
SELECT m.name, p.time, p.date, p.id, 100 - COUNT(r.id) as seats
FROM Projections AS p LEFT JOIN Movies AS m
ON p.movie_id = m.id
left JOIN Reservations AS r ON p.id = r.projection_id
GROUP BY p.id
ORDER BY date ASC;'''

GET_SEATS = '''
SELECT row, col
FROM Reservations
WHERE projection_id = ?;
'''

GET_USER_SEATS = '''
SELECT row, col
FROM Reservations
WHERE projection_id = ? AND user_id = ?;
'''
