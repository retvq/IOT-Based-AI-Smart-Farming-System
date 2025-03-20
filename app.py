from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import os
import ssl

app = Flask(__name__)

# Configure MongoDB URI and secret key
app.config['MONGO_URI'] = 'mongodb+srv://arpulivarthi:Invincible@agriculture.8q4ba1p.mongodb.net/AgriHackretryWrites=true&w=majority'
app.config['SECRET_KEY'] = 'your_secret_key'
# Create a PyMongo instance with ssl_ca_certs
mongo = PyMongo(app)


# ... (rest of your code)

try:
    # Use the mongo object to interact with the database
    users = mongo.db.users
    print("MongoDB connection successful.")
except Exception as e:
    print(f"MongoDB connection failed. Error: {e}")

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            if request.form['password'] == request.form['confirm_password']:
                hashed_password = generate_password_hash(request.form['password'], method='sha256')
                users.insert({'username': request.form['username'], 'password': hashed_password})
                flash('Account created successfully! Please log in.', 'success')
                return redirect(url_for('login'))
            else:
                flash('Password and Confirm Password do not match. Please try again.', 'danger')
        else:
            flash('Username already exists. Please choose a different one.', 'danger')

    return render_template('signup.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'username': request.form['username']})

        if login_user and check_password_hash(login_user['password'], request.form['password']):
            session['username'] = request.form['username']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        flash('You are not logged in. Please log in first.', 'danger')
        return redirect(url_for('login'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
