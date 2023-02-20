from flask import Blueprint, render_template, url_for, request, redirect, flash, session
from app.models import User, Item, db	
from sqlalchemy import desc

views = Blueprint('views', __name__)

# Home View Route ==============================
@views.route('/home', methods=['POST', 'GET'])
def home():
	# Variables
	user = User.query.filter_by(username='Kianu').first()
	items = Item.query.filter_by(user_id = user.id).order_by(desc(Item.id))
	session_user = session['user']

	# Adding a product
	if request.method == 'POST' and request.form.get('add') and "user" in session:
		# print(request.form.get('search-bar'))
		product = request.form.get('product')
		bar_code = request.form.get('bar_code')
		cost = request.form.get('cost')
		selling = request.form.get('selling')
		action = request.form.get('action')
		

		if product != '' and bar_code != '' and cost != '' and selling != '' and action != '':
			new_item = Item(bar_code=bar_code, product=product, cost=cost, selling=selling, action=action, user=user)
			db.session.add(new_item)
			db.session.commit()
			flash(f'Added {product}')
			items = Item.query.filter_by(user_id = user.id).order_by(desc(Item.id))
		else:
			flash('Fill All Inputs')
			return redirect('home')

	# Searching a Product
	elif request.method == 'POST' and request.form.get('search-bar'):
		search = request.form.get('search')
		if search == '' or search == 'all':
			items = Item.query.filter_by(user_id = user.id).order_by(desc(Item.id))
		elif search != '':
			items = Item.query.filter_by(user_id = user.id, product=search)

	return render_template('home.html', title='Home Page', user=user, items=items, session_user = session['user'])



# Delete an Item Route ================
@views.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):

	item = Item.query.filter_by(id=id).first()
	db.session.delete(item)
	db.session.commit()

	return redirect(url_for('views.home'))
	# return item.product