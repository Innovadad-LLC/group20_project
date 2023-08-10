from database.db import Database
from core.session import Sessions
from app import app, db, sessions, username

username = 'testuser'
db = Database('database/store_records.db')
products = db.get_full_inventory()
sessions = Sessions()
sessions.add_new_session(username, db)

def test_index_route():
    """
    Tests that the index route can be retrieved properly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    response = app.test_client().get('/')

    if response.status_code == 200:
        return True, "Success"
    else:
        return False, "Error retrieving index route."
    
def test_login_route():
    """
    Tests that the login route can be retrieved properly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    response = app.test_client().get('/login')

    if response.status_code == 200:
        return True, "Success"
    else:
        return False, "Error retrieving login route."
    
def test_logout_route():
    """
    Tests that the logout route can be retrieved properly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    response = app.test_client().get('/logout')

    if response.status_code == 200:
        return True, "Success"
    else:
        return False, "Error retrieving logout route."
    
def test_home_route():
    """
    Tests that the home route can be retrieved properly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    response = app.test_client().post('/home', data={'username': username, 'password': 'password'})

    if response.status_code == 200:
        return True, "Success"
    else:
        return False, "Error retrieving home route."
    
def test_register_route():
    """
    Tests that the register route can be retrieved properly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    response = app.test_client().get('/register')

    if response.status_code == 200:
        return True, "Success"
    else:
        return False, "Error retrieving register route."
    
def test_checkout_route():
    """
    Tests that the checkout route can be retrieved properly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    response = app.test_client().post('/checkout', data={'1': 1}, headers={'Content-Type': 'application/x-www-form-urlencoded;boundary=BOUNDARY'})

    if response.status_code == 200:
        return True, "Success"
    else:
        return False, "Error retrieving checkout route."