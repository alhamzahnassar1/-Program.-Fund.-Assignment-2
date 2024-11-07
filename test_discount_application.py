# test_discount_application.py
from ebook_store import Customer, Ebook, ShoppingCart, Order


def test_discount_application():
    # Create e-books to add to the cart
    ebook1 = Ebook("Harry Potter", "JK Rowling", "1999-01-12", "Fantasy", 29.99)
    ebook2 = Ebook("Lord Of The Rings", "John Ronald Reuel Tolkien", "1987-02-09", "Fantasy", 39.99)
    ebook3 = Ebook("Rich Dad Poor Dad", "Robert Kiyosaki", "1997-02-04", "Philosophy", 49.99)
    ebook4 = Ebook("Diary Of A Wimpy Kid", "Jeff Kinney", "2000-01-06", "Children", 59.99)
    ebook5 = Ebook("Matilda", "Roald Dahl.", "1987-08-11", "Children", 69.99)

    # Initialize a shopping cart and add e-books
    cart = ShoppingCart()
    cart.addItem(ebook1)
    cart.addItem(ebook2)
    cart.addItem(ebook3)
    cart.addItem(ebook4)
    cart.addItem(ebook5)

    # Show cart contents and total before applying discounts
    print("\nShopping cart contents before applying discounts:")
    print(cart)
    print(f"Total price: ${cart.calculateTotal():.2f}")

    # Create a customer who is a loyalty program member
    customer = Customer("Alice", "alice@example.com", is_loyalty_member=True)

    # Create an order with the shopping cart items for a loyalty program member
    print("\nCreating an order for a loyalty program member...")
    order = Order(customer, cart.items)
    order.applyDiscount()  # Applies a 10% loyalty discount for Alice
    print(f"Total after loyalty discount: ${order.amount:.2f}")

    # Show total with loyalty discount applied
    print("\nCreating an order for a bulk purchase (5 or more items)...")
    bulk_order = Order(customer, cart.items)
    bulk_order.applyDiscount()  # Applies a 20% bulk discount
    print(f"Total after bulk discount: ${bulk_order.amount:.2f}")


# Run the test
if __name__ == "__main__":
    test_discount_application()

OUTPUT:

C:\Users\alham\PycharmProjects\pythonProject\.venv\Scripts\python.exe C:\Users\alham\PycharmProjects\pythonProject\test_discount_application.py 
Added Harry Potter to cart.
Added Lord Of The Rings to cart.
Added Rich Dad Poor Dad to cart.
Added Diary Of A Wimpy Kid to cart.
Added Matilda to cart.

Shopping cart contents before applying discounts:
ShoppingCart(items=['Ebook(title=Harry Potter, author=JK Rowling, price=29.99)', 'Ebook(title=Lord Of The Rings, author=John Ronald Reuel Tolkien, price=39.99)', 'Ebook(title=Rich Dad Poor Dad, author=Robert Kiyosaki, price=49.99)', 'Ebook(title=Diary Of A Wimpy Kid, author=Jeff Kinney, price=59.99)', 'Ebook(title=Matilda, author=Roald Dahl., price=69.99)'])
Total price: $249.95

Creating an order for a loyalty program member...
Total after loyalty discount: $199.96

Creating an order for a bulk purchase (5 or more items)...
Total after bulk discount: $199.96

Process finished with exit code 0

