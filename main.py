from flask import Flask, request, session, redirect, url_for, render_template, flash

import pymysql
import re

from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

mysql = MySQL()

# initializing a variable of Flask
app = Flask(__name__, template_folder="templates")
app.secret_key = 'cairocoders-ednalan'

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'garden'
mysql.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        print(password)

        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM staff WHERE username = %s', (username,))
        # Fetch one record and return result
        account = cursor.fetchone()

        # If account exists in accounts table in out database
        if account:
            password_rs = account['password']
            print(password_rs)
            # If account exists in users table in out database
            if check_password_hash(password_rs, password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['username'] = account['username']
                # Redirect to home page
                return redirect(url_for('profile'))
            else:
                # Account doesnt exist or username/password incorrect
                flash('Incorrect username/ password')
        else:
            # Account doesnt exist or username/password incorrect
            flash('Incorrect username/ password')

    return render_template('login.html')


@app.route('/new', methods=['GET', 'POST'])
def new_user():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # Check if "username", "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        _hashed_password = generate_password_hash(password)

        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM staff WHERE username = %s', (username,))
        account = cursor.fetchone()
        print(account)
        # If account exists show error and validation checks
        if account:
            flash('Account already exists!')
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Username must contain only characters and numbers!')
        elif not username or not password:
            flash('Please fill out the form!')
        else:
            # Account doesnt exists and the form data is valid, now insert new account into users table
            cursor.execute("INSERT INTO staff (username, password) VALUES (%s,%s)",
                           (username, _hashed_password))
            conn.commit()
            flash('You have successfully registered!')
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        flash('Please fill out the form!')
    # Show registration form with message (if any)
    return render_template('register.html')


@app.route('/new/profile', methods=['GET'])
def profile():
    if 'loggedin' in session:
        username = session['username']
        con = mysql.connect()  # set up database connection
        cur = con.cursor()
        cur.execute('SELECT name, address, date_work, requirement FROM customer WHERE username = %s', (username,))
        rows = cur.fetchall()
        con.commit()
    return render_template("profile.html", username=session['username'], rows=rows)


@app.route('/new/logout')
def logout():
    return redirect(url_for('index'))


@app.route('/newcustomer')
def new_customer():
    return render_template("newcustomer.html", username=session['username'])


@app.route('/register_customer', methods=['POST', 'GET'])
def register_customer():
    if request.method == "POST":
        if "name" in request.form and "address" in request.form and "date_work" in request.form and "requirement" \
                in request.form:
            username = session['username']
            name = request.form['name']  # retrieve form data
            address = request.form['address']
            date_work = request.form['date_work']
            requirement = request.form['requirement']
            con = mysql.connect()  # set up database connection
            cur = con.cursor()
            cur.execute("INSERT INTO garden.customer(username, name, address, date_work, requirement) "
                        "VALUES(%s,%s,%s,%s,%s)",
                        (username, name, address, date_work, requirement))
            con.commit()
        return redirect(url_for('profile'))
    return render_template("newcustomer.html")


@app.route('/remove', methods=['POST', 'GET'])
def remove():
    if request.method == 'POST':
        if "name" in request.form:
            name = request.form['name']
            con = mysql.connect()
            cur = con.cursor()
            cur.execute('DELETE FROM garden.customer WHERE name=%s', name)
            con.commit()
            con.close()
        return redirect(url_for('profile'))
    return render_template("remove.html")


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        if "name" in request.form and "address" in request.form:
            name = request.form['name']
            address = request.form['address']
            con = mysql.connect()
            cur = con.cursor()
            cur.execute("UPDATE garden.customer SET address=%s WHERE name=%s", (address, name))
            con.commit()
            con.close()
        return redirect(url_for('profile'))
    return render_template("update.html")


if __name__ == '__main__':
    app.run(debug=True)
