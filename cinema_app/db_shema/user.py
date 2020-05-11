FETCH_USER = '''
SELECT id, email FROM User WHERE email=? AND password=?;
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
