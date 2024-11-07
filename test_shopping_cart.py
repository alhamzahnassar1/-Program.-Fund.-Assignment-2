# test_shopping_cart.py
from ebook_store import ShoppingCart, Ebook

def test_shopping_cart_management():
    # Initialize shopping cart
    cart = ShoppingCart()

    # Create e-books to add to the cart
    ebook1 = Ebook("Harry Potter", "JK Rowling", "1999-01-12", "Fantasy", 29.99)
    ebook2 = Ebook("Lord Of The Rings", "John Ronald Reuel Tolkien", "1987-02-09", "Fantasy", 39.99)
    ebook3 = Ebook("Rich Dad Poor Dad", "Robert Kiyosaki", "1997-02-04", "Philosophy", 49.99)

    # Add e-books to the shopping cart
    print("\nAdding e-books to the shopping cart:")
    cart.addItem(ebook1)
    cart.addItem(ebook2)
    cart.addItem(ebook3)

    # Show cart contents and total after adding items
    print("\nShopping cart contents after adding e-books:")
    print(cart)
    print(f"Total price: ${cart.calculateTotal():.2f}")

    # Remove an e-book from the shopping cart
    print("\nRemoving an e-book from the shopping cart:")
    cart.removeItem(ebook2)

    # Show cart contents and total after removal
    print("\nShopping cart contents after removing an e-book:")
    print(cart)
    print(f"Total price: ${cart.calculateTotal():.2f}")

# Run the test
if __name__ == "__main__":
    test_shopping_cart_management()

OUTPUT:

C:\Users\alham\PycharmProjects\pythonProject\.venv\Scripts\python.exe C:\Users\alham\PycharmProjects\pythonProject\test_shopping_cart.py 

Adding e-books to the shopping cart:
Added Harry Potter to cart.
Added Lord Of The Rings to cart.
Added Rich Dad Poor Dad to cart.

Shopping cart contents after adding e-books:
ShoppingCart(items=['Ebook(title=Harry Potter, author=JK Rowling, price=29.99)', 'Ebook(title=Lord Of The Rings, author=John Ronald Reuel Tolkien, price=39.99)', 'Ebook(title=Rich Dad Poor Dad, author=Robert Kiyosaki, price=49.99)'])
Total price: $119.97

Removing an e-book from the shopping cart:
Removed Lord Of The Rings from cart.

Shopping cart contents after removing an e-book:
ShoppingCart(items=['Ebook(title=Harry Potter, author=JK Rowling, price=29.99)', 'Ebook(title=Rich Dad Poor Dad, author=Robert Kiyosaki, price=49.99)'])
Total price: $79.98

Process finished with exit code 0
