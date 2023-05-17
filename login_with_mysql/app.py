from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
#from passlib.hash import scrypt

from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cpgrams:rajnath@localhost/cpgrams'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'cpgrams'
app.config['MYSQL_PASSWORD'] = 'rajnath'
app.config['MYSQL_DB'] = 'cpgrams'

mysql = MySQL(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        rem=request.form.get('remember')
        if rem is not None:
            rem=1
        else:
            rem=0

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        #password_hash = scrypt.using(rounds=8, salt_size=16).hash(request.form['password'])
        if user and check_password_hash(user[2], password):
        #print(username, password, password_hash, user[2])
        #if user and scrypt.verify(user[2], password):
        # Login successful, redirect to the dashboard or home page
            return redirect('/dashboard')
        else:
            # Login failed, display an error message
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password_hash = generate_password_hash(request.form['password'], method='sha256')
        #password_hash = scrypt.using(rounds=8, salt_size=16).hash(request.form['password'])
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (%s, %s)', (username, password_hash))
        mysql.connection.commit()
        
        return redirect('/login')  # Redirect to the login page after successful signup
    
    return render_template('signup.html')



if __name__ == '__main__':
    app.run()

