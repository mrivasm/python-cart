Shopping Cart Application Documentation
Overview
This documentation provides an overview of the Shopping Cart Application developed using Flask. The application includes user authentication, product browsing, shopping cart management, checkout, and admin features for managing products and categories.

Table of Contents
Requirements
Setup and Installation
Application Structure
Routes
Admin Features
Templates
Usage
Requirements
Python 3.x
Flask
Bootstrap (for front-end design)
Setup and Installation
Clone the Repository
bash
Copy code
git clone https://github.com/mrivasm/python-cart.git
cd <repository-directory>
Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies
bash
Copy code
pip install Flask
Run the Application
bash
Copy code
python app.py
Access the Application
Open your web browser and navigate to http://127.0.0.1:5000/.

Application Structure
arduino
Copy code
shopping-cart/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── category.html
│   ├── cart.html
│   ├── checkout.html
│   ├── receipt.html
│   ├── register.html
│   ├── login.html
│   ├── search.html
│   ├── admin.html
│   ├── add_product.html
│   ├── edit_product.html
│   ├── add_category.html
│   ├── edit_category.html
│
├── app.py
├── models.py
└── README.md
Routes
User Authentication
Register
GET /register: Display the registration form.
POST /register: Handle the user registration.
Login
GET /login: Display the login form.
POST /login: Handle user login.
Logout
GET /logout: Log the user out and redirect to the home page.
Product and Category Browsing
Home
GET /: Display the list of products and categories.
Category
GET /category/<category_name>: Display products in a specific category.
Search
GET /search: Display the search form.
POST /search: Handle product search and display results.
Shopping Cart Management
View Cart
GET /cart: Display the user's shopping cart.
Add to Cart
GET /add_to_cart/<int:product_id>: Add a product to the cart.
Remove from Cart
GET /remove_from_cart/<int:product_id>: Remove a product from the cart.
Checkout and Receipt
Checkout
GET /checkout: Display the checkout form.
POST /checkout: Handle checkout and generate the receipt.
Receipt
GET /receipt: Display the receipt for the completed order.
Admin Features
Admin Dashboard
GET /admin: Display the admin dashboard.
Add Product
GET /admin/add_product: Display the add product form.
POST /admin/add_product: Handle adding a new product.
Edit Product
GET /admin/edit_product/<int:product_id>: Display the edit product form.
POST /admin/edit_product/<int:product_id>: Handle editing a product.
Delete Product
POST /admin/delete_product/<int:product_id>: Handle deleting a product.
Add Category
GET /admin/add_category: Display the add category form.
POST /admin/add_category: Handle adding a new category.
Edit Category
GET /admin/edit_category/<string:category_name>: Display the edit category form.
POST /admin/edit_category/<string:category_name>: Handle editing a category.
Delete Category
POST /admin/delete_category/<string:category_name>: Handle deleting a category.
Templates
Base Template
base.html: The base template that includes common elements like the header, footer, and navigation bar.
User Templates
index.html: Home page displaying products and categories.
category.html: Displays products within a specific category.
cart.html: Displays the user's shopping cart.
checkout.html: Displays the checkout form.
receipt.html: Displays the receipt after checkout.
register.html: User registration form.
login.html: User login form.
search.html: Displays search results.
Admin Templates
admin.html: Admin dashboard.
add_product.html: Form for adding a new product.
edit_product.html: Form for editing a product.
add_category.html: Form for adding a new category.
edit_category.html: Form for editing a category.
Usage
Register
Navigate to /register to create a new user account.
Fill in the registration form and submit.
Login
Navigate to /login to log in to your account.
Enter your username and password and submit.
Browse Products
View products on the home page or by category.
Use the search form to find specific products.
Manage Shopping Cart
Add products to your cart from the product listings.
View your cart at /cart.
Remove products from your cart as needed.
Checkout
Navigate to /checkout to review your order and enter payment details.
Submit the form to complete the purchase.
View the receipt at /receipt.
Admin Features
Log in as an admin user (admin/password).
Access the admin dashboard at /admin.
Add, edit, or delete products and categories.
This documentation provides an overview of the main features and usage of the Shopping Cart Application. For further details and code, refer to the source files in the repository.