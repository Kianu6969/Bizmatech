from flask import Blueprint, render_template, url_for, request, redirect
from app.models import User, Item, db	

views = Blueprint('views', __name__)

@views.route('/home', methods=['POST', 'GET'])
def home():
	user = User.query.filter_by(username='Kianu').first()

	if request.method == 'POST':

		product = request.form.get('product')
		bar_code = request.form.get('bar_code')
		cost = request.form.get('cost')
		selling = request.form.get('selling')
		action = request.form.get('action')

		new_item = Item(bar_code=bar_code, product=product, cost=cost, selling=selling, action=action, user=user)
		db.session.add(new_item)
		db.session.commit()
		print(product);

	return render_template('home.html', title='Home Page', user=user)

# Delete an Item
@views.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):

	item = Item.query.filter_by(id=id).first()
	db.session.delete(item)
	db.session.commit()

	return redirect(url_for('views.home'))
	# return item.product