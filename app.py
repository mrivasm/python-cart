from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import Product, User, ShoppingCart

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Ensure this is a secure and unique key

# In-memory user storage
users = {}

# Sample product data
products = [
    Product(1, 'Running Shoes', 50.0, 'Footwear'),
    Product(2, 'Leather Boots', 120.0, 'Footwear'),
    Product(3, 'Sandals', 30.0, 'Footwear'),
    Product(4, 'Jeans', 40.0, 'Clothing'),
    Product(5, 'T-Shirt', 20.0, 'Clothing'),
    Product(6, 'Jacket', 70.0, 'Clothing'),
    Product(7, 'Sunglasses', 25.0, 'Accessories'),
    Product(8, 'Watch', 150.0, 'Accessories'),
    Product(9, 'Belt', 15.0, 'Accessories'),
    Product(10, 'Hat', 20.0, 'Accessories'),
]

# Shopping cart
cart = ShoppingCart()


@app.route('/')
def index():
    categories = ['Footwear', 'Clothing', 'Accessories']
    return render_template('index.html', products=products, categories=categories)


@app.route('/category/<category_name>')
def category(category_name):
    try:
        category_products = [
            product for product in products if product.category == category_name]
        return render_template('category.html', category=category_name, products=category_products)
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        flash('An error occurred while trying to load the category.', 'danger')
        return redirect(url_for('index'))


@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'username' not in session:
        flash('You need to login first.', 'danger')
        return redirect(url_for('login'))

    product = next((p for p in products if p.id == product_id), None)
    if product:
        cart.add_product(product)
    return redirect(url_for('index'))


@app.route('/cart')
def view_cart():
    total = cart.get_total()
    return render_template('cart.html', cart=cart.items, total=total)


@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart.remove_product(product_id)
    return redirect(url_for('view_cart'))


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'username' not in session:
        flash('You need to login first.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Store the cart items in session before clearing
        # Convert Product objects to dicts
        session['receipt_cart'] = [item.__dict__ for item in cart.items]
        cart.clear_cart()  # Clear cart after storing
        flash('Payment successful! Your receipt will be generated.', 'success')
        return redirect(url_for('receipt'))

    total = cart.get_total()
    return render_template('checkout.html', cart=cart.items, total=total)


@app.route('/receipt')
def receipt():
    if 'username' not in session:
        flash('You need to login first.', 'danger')
        return redirect(url_for('login'))

    # Retrieve the cart from the session
    receipt_cart = session.pop('receipt_cart', None)
    if not receipt_cart:
        flash('No receipt available. Please complete the checkout process.', 'danger')
        return redirect(url_for('index'))

    # Convert dicts back to Product objects using the from_dict method
    receipt_cart = [Product.from_dict(item) for item in receipt_cart]
    total = sum(item.price for item in receipt_cart)
    return render_template('receipt.html', cart=receipt_cart, total=total)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists.', 'danger')
        else:
            users[username] = User(username, password)
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.get(username)
        if user and user.check_password(password):
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
               in product.name.lower()]
    return render_template('search.html', query=query, results=results)


if __name__ == '__main__':
    app.run(debug=True)
