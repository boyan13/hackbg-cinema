CREATE_TEMP_USER = '''
CREATE TABLE temp_user(
id INTEGER NOT NULL,
email VARCHAR(50),
FOREIGN KEY (id) REFERENCES User(id)
);
'''

GET_TEMP_USER = '''
SELECT * FROM temp_user;
'''

INSERT_TEMP_USER = '''
INSERT INTO temp_user (id, email)
VALUES (?, ?);
'''

DROP_TABLE = '''DROP TABLE IF EXISTS temp_user;'''
