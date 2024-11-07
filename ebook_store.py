# ebook_store.py

class Ebook:
    def __init__(self, title, author, publication_date, genre, price):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.genre = genre
        self.price = price

    def getPrice(self):
        return self.price

    def __str__(self):
        return f"Ebook(title={self.title}, author={self.author}, price={self.price})"


class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info


class Customer(User):
    def __init__(self, name, contact_info, is_loyalty_member=False):
        super().__init__(name, contact_info)
        self.is_loyalty_member = is_loyalty_member

    def __str__(self):
        return f"Customer(name={self.name}, contact_info={self.contact_info}, loyalty_member={self.is_loyalty_member})"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def addItem(self, ebook):
        self.items.append(ebook)
        print(f"Added {ebook.title} to cart.")

    def removeItem(self, ebook):
        if ebook in self.items:
            self.items.remove(ebook)
            print(f"Removed {ebook.title} from cart.")
        else:
            print(f"{ebook.title} not in cart.")

    def calculateTotal(self):
        return sum(item.getPrice() for item in self.items)

    def __str__(self):
        return f"ShoppingCart(items={[str(item) for item in self.items]})"


class Transaction:
    def __init__(self, amount):
        self.amount = amount
        self.status = "Pending"

    def process(self):
        if self.amount > 0:
            self.status = "Completed"
        else:
            self.status = "Failed"


class Order(Transaction):
    VAT_RATE = 0.08
    LOYALTY_DISCOUNT = 0.10
    BULK_DISCOUNT = 0.20

    def __init__(self, customer, ebooks):
        self.customer = customer
        self.ebooks = ebooks
        amount = sum(book.getPrice() for book in ebooks)
        super().__init__(amount)

    def applyDiscount(self):
        if len(self.ebooks) >= 5:
            self.amount *= (1 - self.BULK_DISCOUNT)
        elif self.customer.is_loyalty_member:
            self.amount *= (1 - self.LOYALTY_DISCOUNT)

    def applyVAT(self):
        self.amount *= (1 + self.VAT_RATE)

    def __str__(self):
        return f"Order(customer={self.customer}, amount={self.amount}, status={self.status})"


class Invoice:
    def __init__(self, order):
        self.order = order

    def generateInvoice(self):
        items = "\n".join([f"{ebook.title} - ${ebook.getPrice():.2f}" for ebook in self.order.ebooks])
        total_line = f"Total after discounts and VAT: ${self.order.amount:.2f}"
        return f"Invoice for {self.order.customer.name}:\n{items}\n{total_line}"

    def __str__(self):
        return self.generateInvoice()


class Catalog:
    def __init__(self):
        self.ebooks = []

    def addEbook(self, ebook):
        self.ebooks.append(ebook)
        print(f"Added {ebook.title} to the catalog.")

    def removeEbook(self, ebook):
        if ebook in self.ebooks:
            self.ebooks.remove(ebook)
            print(f"Removed {ebook.title} from the catalog.")
        else:
            print(f"{ebook.title} not found in the catalog.")

    def __str__(self):
        return f"Catalog(ebooks={[str(ebook) for ebook in self.ebooks]})"


class LoyaltyProgram:
    def __init__(self):
        self.members = set()

    def addMember(self, customer):
        self.members.add(customer)
        customer.is_loyalty_member = True
        print(f"{customer.name} has been added to the loyalty program.")




OUTPUT:
N/A
