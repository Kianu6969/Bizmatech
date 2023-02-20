from flask import Blueprint, render_template, url_for, request, redirect, flash
from app.models import User

auth = Blueprint('auth', __name__)

# User login 
@auth.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		name = request.form.get('username')
		password = request.form.get('password')
		user = User.query.filter_by(username=name, password=password).first()

		if user:
			flash('You have logged in!')
			return redirect(url_for('views.home'))

		else:
			return redirect(url_for('auth.login'))
			
	return render_template('login.html', title='Login Page')


# When User logs out
@auth.route('/logout')
def logout():
	return render_template('login.html', title='Logout Page')
