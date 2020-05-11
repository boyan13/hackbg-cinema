MAKE_RESERVETION = '''
INSERT INTO Reservations(user_id, projection_id, row, col)
VALUES (?, ?, ?, ?);'''

DELETE_RESERVATION = '''
DELETE FROM Reservations
WHERE user_id = ? AND projection_id = ? AND row = ? AND col = ?;
'''
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

GET_USER_RESERVATIONS = '''
SELECT r.row, r.col, m.name, p.time, p.date, p.id, r.ID
FROM Reservations AS r LEFT JOIN
Projections AS p ON r.projection_id = p.id LEFT JOIN Movies AS m
ON p.movie_id = m.id
WHERE r.user_id =  ?;
'''
