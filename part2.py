class Product:
    def __init__(self, name, price):
        self.name = name
        self.price= price

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)


    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

# Create products
food= Product("Chicken ", 10000)
phone = Product("iphone 16", 500)
bag= Product("spongebob", 500)

# Create a cart
cart = Cart()

# Add items to the cart
cart.add_item(food)
cart.add_item(phone)
cart.add_item(bag)

# Calculate and print the total
print("Total:", cart.calculate_total())