# PROVIDE 2 ARGS (Email and Passowrd).
# Return ID and EMAIL
# if EMAIL and PASSWORD arguments match any.
FETCH_USER = '''
SELECT id, email FROM User WHERE email=? AND password=?;
'''
