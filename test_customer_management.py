# test_customer_management.py
from ebook_store import Customer, LoyaltyProgram

def test_customer_management():
    # Initialize a loyalty program
    loyalty_program = LoyaltyProgram()

    # Add a new customer
    customer1 = Customer("Al Hamzah Nassar", "alhamzahnassar@gmail.com.com", is_loyalty_member=False)
    customer2 = Customer("Adnan Daher", "adnandaher@gmail.com", is_loyalty_member=False)
    print("\nAdding new customers:")
    print(customer1)
    print(customer2)

    # Add customers to the loyalty program
    print("\nAdding Al Hamzah Nassar to the loyalty program...")
    loyalty_program.addMember(customer1)

    # Show updated customer information
    print("\nCustomer information after adding to loyalty program:")
    print(customer1)
    print(customer2)

    # Modify customer information
    print("\nModifying Adnan Daher's contact information...")
    customer2.contact_info = "adnandaher01@gmail.com"
    print("Updated customer information for Adnan Daher:")
    print(customer2)

    # Simulate removing a customer (simply by setting to None or ignoring further use in this test)
    print("\nRemoving customer Al Hamzah Nassar from the system...")
    del customer1  # Note: In a real system, we would remove references and clear data.

    print("\nRemaining customer information in the system:")
    print(customer2)

# Run the test
if __name__ == "__main__":
    test_customer_management()


OUTPUT:

C:\Users\alham\PycharmProjects\pythonProject\.venv\Scripts\python.exe C:\Users\alham\PycharmProjects\pythonProject\test_customer_management.py 

Adding new customers:
Customer(name=Al Hamzah Nassar, contact_info=alhamzahnassar@gmail.com.com, loyalty_member=False)
Customer(name=Adnan Daher, contact_info=adnandaher@gmail.com, loyalty_member=False)

Adding Al Hamzah Nassar to the loyalty program...
Al Hamzah Nassar has been added to the loyalty program.

Customer information after adding to loyalty program:
Customer(name=Al Hamzah Nassar, contact_info=alhamzahnassar@gmail.com.com, loyalty_member=True)
Customer(name=Adnan Daher, contact_info=adnandaher@gmail.com, loyalty_member=False)

Modifying Adnan Daher's contact information...
Updated customer information for Adnan Daher:
Customer(name=Adnan Daher, contact_info=adnandaher01@gmail.com, loyalty_member=False)

Removing customer Al Hamzah Nassar from the system...

Remaining customer information in the system:
Customer(name=Adnan Daher, contact_info=adnandaher01@gmail.com, loyalty_member=False)

Process finished with exit code 0
