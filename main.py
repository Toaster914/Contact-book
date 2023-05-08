'''
Contact Book
Evan Hanrahan
5/8/23
Python 2
'''

import contact_book

def manipulate_book(name):
    '''
    Handles the menu for contact book
    manipulation.
    '''
    action = ""
    while action != "quit":
        action = input("Add, remove, or get a contact (\"quit\" to exit) >> ").lower()
        if action == "add":
            person_name = input("Enter the name of the contact >> ")
            phone = input("Enter the phone number of the contact >> ")
            contact_book.add_contact(person_name, phone)
        elif action == "remove":
            person_name = input("Enter the name of the contact to remove >> ")
            if contact_book.remove_contact(person_name):
                print("Success, Person removed.")
            else:
                print("Failure. Person does not exist.")
        elif action == "get":
            person_name = input("Enter the name of the contact to get >> ")
            print(contact_book.get_contact(person_name))
        elif action != "quit":
            print("Invalid action.")

action = ""
while action != "quit":
    action = input("Create or open a contact book? (\"quit\" to exit) >> ").lower()
    if action == "create":
        name = input("Enter your last name >> ")
        if contact_book.create_book(name):
            print("Successfuly created contact book >> ")
        else:
            print("Contact book already exists.")

    elif action == "open":
        name = input("Enter your last name >> ")
        if contact_book.open_book(name):
            manipulate_book(name)
        else:
            print("Contact does not eixist.")
    elif action != "quit":
        print("invalid action.")
