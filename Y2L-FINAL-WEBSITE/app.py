#broken pipe fix
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 
#

from databases import *
from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

@app.route("/", methods=['GET', 'POST'])
def sign_in():
	return render_template('sign_in.html')


@app.route("/alphabet", methods=['GET', 'POST'])
def alphabet():
	user = get_user(login_session['name'])
	return render_template('alphabet.html', user = user, letters = letters)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		email = request.form['email']
		username = request.form['username']
		password = request.form['password']
		print(first_name, last_name, email, username, password)
		register_user(first_name = first_name, last_name = last_name, email = email, username = username, password = password)
		user = get_user(username)
		return render_template("alphabet.html", user=user, letters = letters)

	return render_template("sign_up.html")

@app.route("/user_login", methods = ['POST'])
def user_login():
	user = get_user(request.form['username_inp'])
	print(user)
	if user and user.verify_password(request.form['password_inp']):
		print(user)
		login_session['name'] = user.username
		login_session['logged_in'] = True
		return render_template("alphabet.html", user = user, letters = letters)
	else:
		return render_template("sign_in.html")

@app.route("/test", methods=['GET', 'POST'])
def test():
	user = get_user(login_session['name'])
	return render_template('fingerspell_test.html', user = user)


if __name__ == '__main__':
    app.run(debug=True)