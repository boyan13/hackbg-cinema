# PROVIDE 2 ARGS (Email and Passowrd).
# Return ID and EMAIL
# if EMAIL and PASSWORD arguments match any.
FETCH_USER = '''
SELECT id, email FROM User WHERE email=? AND password=?;
'''

MOVIES = '''
CREATE TABLE IF NOT EXISTS  Movies (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(100) NOT NULL,
rating REAL NOT NULL DEFAULT 0 CHECK (rating BETWEEN 0 AND 10)
);
'''
USERS = '''
CREATE TABLE IF NOT EXISTS  User (
id INTEGER PRIMARY KEY AUTOINCREMENT,
email VARCHAR(50) UNIQUE NOT NULL,
password VARCHAR(130) NOT NULL
);
'''

CLIENT = '''
CREATE TABLE IF NOT EXISTS  Client (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER UNIQUE NOT NULL,
FOREIGN KEY (user_id) REFERENCES User(id)
);
'''

EMPLOYEE = '''
CREATE TABLE IF NOT EXISTS  Empoyee (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER UNIQUE NOT NULL,
FOREIGN KEY (user_id) REFERENCES User(id)
);
'''

PROJECTIONS = '''
CREATE TABLE IF NOT EXISTS  Projections (
id INTEGER PRIMARY KEY AUTOINCREMENT,
movie_id INTEGER NOT NULL,
type VARCHAR(5),
date VARCHAR(10) NOT NULL,
time VARCHAR(5) NOT NULL,
FOREIGN KEY (movie_id) REFERENCES Movies(id)
);
'''

RESERVATIONS= '''
CREATE TABLE IF NOT EXISTS  Reservations (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
projection_id INTEGER NOT NULL,
row INTEGER NOT NULL CHECK (row BETWEEN 1 AND 10),
col INTEGER NOT NULL CHECK (col BETWEEN 1 AND 10),
FOREIGN KEY (user_id) REFERENCES User(id),
FOREIGN KEY (projection_id) REFERENCES Projection(id)
);
'''

CREATE_USER = '''
INSERT INTO User (email, password)
VALUES (?, ?);
'''

CREATE_CLIENT = '''
INSERT INTO Client (user_id)
VALUES (?);
'''

GET_USER_ID = '''SELECT id FROM User WHERE email = ?'''

ADD_MOVIE = '''
INSERT INTO MOVIES (name, rating)
VALUES (?, ?);
'''

SHOW_MOVIES = '''
SELECT * FROM MOVIES ORDER BY rating DESC;'''

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

GET_MOVIE_BY_ID = '''
SELECT *
FROM Movies
WHERE id = ?;'''

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
