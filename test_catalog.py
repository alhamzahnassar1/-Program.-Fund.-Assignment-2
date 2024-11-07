# test_catalog.py
from ebook_store import Catalog, Ebook

def test_catalog_management():
    # Initialize catalog
    catalog = Catalog()

    # Add a new e-book to the catalog
    ebook1 = Ebook("Harry Potter", "JK Rowling", "1999-01-12", "Fantasy", 29.99)
    ebook2 = Ebook("Lord Of The Rings", "John Ronald Reuel Tolkien", "1973-02-9", "Fantasy", 39.99)
    catalog.addEbook(ebook1)
    catalog.addEbook(ebook2)

    # Show catalog contents
    print("\nCatalog contents after adding two e-books:")
    print(catalog)

    # Modify the price of an e-book in the catalog
    print("\nModifying price of the first e-book...")
    ebook1.price = 24.99
    print(f"Updated {ebook1.title} price to ${ebook1.price:.2f}")

    # Show catalog contents after modification
    print("\nCatalog contents after modifying e-book price:")
    print(catalog)

    # Remove an e-book from the catalog
    print("\nRemoving an e-book from the catalog...")
    catalog.removeEbook(ebook1)

    # Show catalog contents after removal
    print("\nCatalog contents after removing an e-book:")
    print(catalog)

# Run the test
if __name__ == "__main__":
    test_catalog_management()


OUTPUT:

C:\Users\alham\PycharmProjects\pythonProject\.venv\Scripts\python.exe C:\Users\alham\PycharmProjects\pythonProject\test_catalog.py 
Added Harry Potter to the catalog.
Added Lord Of The Rings to the catalog.

Catalog contents after adding two e-books:
Catalog(ebooks=['Ebook(title=Harry Potter, author=JK Rowling, price=29.99)', 'Ebook(title=Lord Of The Rings, author=John Ronald Reuel Tolkien, price=39.99)'])

Modifying price of the first e-book...
Updated Harry Potter price to $24.99

Catalog contents after modifying e-book price:
Catalog(ebooks=['Ebook(title=Harry Potter, author=JK Rowling, price=24.99)', 'Ebook(title=Lord Of The Rings, author=John Ronald Reuel Tolkien, price=39.99)'])

Removing an e-book from the catalog...
Removed Harry Potter from the catalog.

Catalog contents after removing an e-book:
Catalog(ebooks=['Ebook(title=Lord Of The Rings, author=John Ronald Reuel Tolkien, price=39.99)'])

Process finished with exit code 0

