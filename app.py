#!/usr/bin/env python3

from authentication.auth_tools import login_pipeline, update_passwords, hash_password, username_exists
from database.db import Database
from flask import Flask, render_template, request
from core.session import Sessions

app = Flask(__name__)
HOST, PORT = 'localhost', 8080
global username, products, db, sessions
username = ''
db = Database('database/store_records.db')
products = db.get_full_inventory()
sessions = Sessions()

@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    global username, sessions
    if sessions.get_session(username) != None:
        sess = sessions.get_session(username)
        sessname = sess.username
        if sessname != None:
            return render_template('home.html', products=products, sessions=sessions, logged_in=True)
    else:
        return render_template('index.html')


@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    global username, sessions
    if sessions.get_session(username) != None:
        sess = sessions.get_session(username)
        sessname = sess.username
        if len(sessname) > 0:
            return render_template('home.html', products=products, sessions=sessions, logged_in=True)
    else:
        return render_template('login.html')

@app.route('/logout')
def logout_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    global username, sessions
    if sessions.get_session(username) != None:
        sessions.remove_session(username)
        username = ''
    return render_template('logout.html')
    
@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    global username, sessions
    username = request.form['username']
    password = request.form['password']
    if len(username) > 0:
        if login_pipeline(username, password):
            sessions.add_new_session(username, db)
            return render_template('home.html', products=products, sessions=sessions, logged_in=True)
        else:
            print(f"Incorrect username ({username}) or password ({password}).")
            return render_template('login.html', error=True)
    else:
        print(f"Incorrect username or password.")
        return render_template('login.html', error=True)


@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/store_records.db: adds a new user to the database
    """
    global username, sessions
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    if not username_exists(username):
        salt, key = hash_password(password)
        update_passwords(username, key, salt)
        db.insert_user(username, key, email, first_name, last_name)
        sessions.add_new_session(username, db)
        return render_template('home.html', products=products, sessions=sessions, logged_in=True)
    else:
        print(f"Username ({username}) is already taken.")
        return render_template('register.html', error=True)


@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """
    global username, sessions
    order = []
    user_session = sessions.get_session(username)
    if user_session != None:
        for item in products:
            print(f"item ID: {item['id']}")
            if request.form.get(str(item['id'])):
                count = request.form.get(str(item['id']))
                order.append({
                    "id": item['id'],
                    "item_name": item['item_name'],
                    "count": float(count),
                    "price": item['price']
                })
                user_session.add_new_item(
                    item['id'], item['item_name'], item['price'], count)

        user_session.submit_cart()
        return render_template('checkout.html', order=order, sessions=sessions, total_cost=user_session.total_cost, logged_in=True)
    else:
        return render_template('home.html', products=products, sessions=sessions, error=True)
    
if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
