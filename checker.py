from flask import session
from functools import wraps

def check_logged_in(func):
    @wraps(func)
    def wrapper(*argc, **kwargs):
        if 'logged_in' in session:
            return func(*argc, **kwargs)
        return 'you are not logged in'
    return wrapper