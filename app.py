# -----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
# -----------------------------------------------------------------------------------------

from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# In-memory user storage
users = {}

# Sample product data
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.00},
    {'id': 2, 'name': 'Product 2', 'price': 15.99},
    {'id': 3, 'name': 'Product 3', 'price': 20.34},
]

# Shopping cart
cart = []


@app.route('/')
def index():
    return render_template('index.html', products=products)


@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'username' not in session:
        flash('You need to login first.', 'danger')
        return redirect(url_for('login'))

    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('index'))


@app.route('/cart')
def view_cart():
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)


@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    global cart
    cart = [item for item in cart if item['id'] != product_id]
    return redirect(url_for('view_cart'))


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'username' not in session:
        flash('You need to login first.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Process payment details here
        flash('Payment successful!', 'success')
        global cart
        cart = []  # Clear cart after successful payment
        return redirect(url_for('index'))

    total = sum(item['price'] for item in cart)
    return render_template('checkout.html', cart=cart, total=total)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists.', 'danger')
        else:
            users[username] = generate_password_hash(password)
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_password_hash = users.get(username)
        if user_password_hash and check_password_hash(user_password_hash, password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query', '')
    results = [product for product in products if query.lower()
               in product['name'].lower()]
    return render_template('search.html', query=query, results=results)


if __name__ == '__main__':
    app.run(debug=True)
