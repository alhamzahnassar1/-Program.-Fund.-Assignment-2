# test_invoice_generation.py
from ebook_store import Customer, Ebook, ShoppingCart, Order, Invoice

def test_invoice_generation():
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

    # Create a customer who is a loyalty program member
    customer = Customer("Alice", "alice@example.com", is_loyalty_member=True)

    # Create an order with the shopping cart items
    order = Order(customer, cart.items)
    print("\nOrder total before discounts and VAT:")
    print(f"${order.amount:.2f}")

    # Apply discounts and VAT
    order.applyDiscount()
    order.applyVAT()
    print("\nOrder total after discounts and VAT:")
    print(f"${order.amount:.2f}")

    # Generate and display invoice
    invoice = Invoice(order)
    print("\n--- Invoice ---")
    print(invoice.generateInvoice())

# Run the test
if __name__ == "__main__":
    test_invoice_generation()

OUTPUT:

C:\Users\alham\PycharmProjects\pythonProject\.venv\Scripts\python.exe C:\Users\alham\PycharmProjects\pythonProject\test_invoice_generation.py 
Added Harry Potter to cart.
Added Lord Of The Rings to cart.
Added Rich Dad Poor Dad to cart.
Added Diary Of A Wimpy Kid to cart.
Added Matilda to cart.

Order total before discounts and VAT:
$249.95

Order total after discounts and VAT:
$215.96

--- Invoice ---
Invoice for Alice:
Harry Potter - $29.99
Lord Of The Rings - $39.99
Rich Dad Poor Dad - $49.99
Diary Of A Wimpy Kid - $59.99
Matilda - $69.99
Total after discounts and VAT: $215.96

Process finished with exit code 0
