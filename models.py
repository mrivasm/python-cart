from werkzeug.security import generate_password_hash, check_password_hash


class Product:
    def __init__(self, product_id, name, price, category):
        self.id = product_id
        self.name = name
        self.price = price
        self.category = category

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data['id'],
            name=data['name'],
            price=data['price'],
            category=data['category']
        )


class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product_id):
        self.items = [item for item in self.items if item.id != product_id]

    def get_total(self):
        return sum(item.price for item in self.items)

    def clear_cart(self):
        self.items = []
