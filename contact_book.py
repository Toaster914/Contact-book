'''
Functions that manage a virtual contact book.
'''

import os
import file_utilities


def create_book(lastname):
    '''
    Creates a contact book file.
    '''
    if os.path.exists(lastname + ".txt"):
        return False
    else:
        file = open(lastname + ".txt", "x")
        file.close
        return True

def open_book(lastname):
    '''
    Opens a contact book file for manipulation.
    '''
    if os.path.exists(lastname + ".txt"):
        global file_name, contact_book
        file_name = lastname + ".txt"
        contact_book = file_utilities.read_lines(file_name)
        return True
    else:
        return False

def add_contact(name, phone):
    '''
    Adds a contact to the contact book file.
    '''
    global contact_book, file_name
    contact_book.append(name + "-" + phone)
    file_utilities.write_lines(contact_book, file_name)

def remove_contact(name):
    '''
    Removes a contact from the contact book file.
    '''
    global contact_book, file_name
    if in_contact_book(name):
        contact = get_contact(name)
        contact_book.remove(contact)
        file_utilities.write_lines(contact_book, file_name)
        return True
    else:
        return False

def get_contact(name):
    '''
    Gets a contact from the contact book file.
    '''
    global contact_book
    for contact in contact_book:
        if name in contact:
            return contact
    return "No contact"

def in_contact_book(name):
    '''
    Checks if the name is in the contact book file.
    '''
    global contact_book
    for contact in contact_book:
        if name in contact:
            return True
    return False
