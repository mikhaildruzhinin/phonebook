#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# phonebook contains names, phone numbers, email adresses and bdays
# user can browse cards in the phonebook, search for a card, add/remove a card

import pickle # using protocol 3 for compatibility
import argparse

class Card():
    phone = ''
    email= ''
    bday = ''
    def __init__(self, phone, email, bday): # creating a new card for the phonebook
        self.phone = phone
        self.email = email
        self.bday = bday
    def __str__(self):
        c = f'phone number: {self.phone}, email adress: {self.email}, bday: {self.bday}'
        return c
    def __repr__(self): 
        return str(self)

class Phonebook():
    phonebook = {}
    def __init__(self):
        pass
    def __str__(self):
        return str(self.phonebook)
    def __repr__(self):
        return str(self)
    def __getstate__(self):
        return self.phonebook
    def __setstate__(self, state):
        self.phonebook = state
    def getphones(self):
        pass
    def getemails(self):
        pass
    def getbdays(self):
        pass
    def browse(self):
        l1 = len(max(('Name:', self.phonebook.keys()), key = len)) + 1
        l2 = len(max(('Phone number', self.phonebook.keys()), key = len)) + 1
        l3 = len(max(('Email', self.phonebook.keys()), key = len)) + 1
        l4 = len(max(('Bday', self.phonebook.keys()), key = len)) + 1
        print('Name'.ljust(l1) + 'Phone number'.ljust(l2) + 'Email'.ljust(l3) + 'Bday')
        print('-' * (l1 + l2 + l3 + l4))
        for i in self.phonebook.keys():
            p = i.ljust(l1) + self.phonebook[i].phone.ljust(l2) + self.phonebook[i].email.ljust(l3) + self.phonebook[i].bday
            print(p)
    def add(self, name, card):
        self.phonebook[name] = card
    def remove(self, name):
        return self.phonebook.pop(name, None)
    def search (self, name):
        if name in self.phonebook:
            return name, self.phonebook[name]
        return f'{name} not found'

parser = argparse.ArgumentParser('')
parser.add_argument('--browse', '-b', dest='phonebook_action', action='store_const', const='browse', default='browse',
                    help='Browsing the phonebook')
parser.add_argument('--add', '-a', dest='phonebook_action', action='store_const', const='add', default='browse',
                    help='Adding a new contact')
parser.add_argument('--remove', '-r', dest='phonebook_action', action='store_const', const='remove', default='browse',
                    help='Removing a contact from the phonebook')
parser.add_argument('--search', '-s', dest='phonebook_action', action='store_const', const='search', default='browse',
                    help='Searching for the contact in the phonebook')

ARGS = parser.parse_args()

# Loading up the phonebook
try:    
    with open('data.txt', 'rb') as f:
        phonebook = pickle.load(f)
except FileNotFoundError:
    phonebook = Phonebook() # creating a new phonebook if there is no pickled one
    print('New phonebook created')
# browsing the phonebook
if ARGS.phonebook_action == 'browse':
    phonebook.browse()
unsaved_changes = False
# adding a new contact
if ARGS.phonebook_action == 'add':
    print('Adding a new contact')
    name = input('Input a name: ')
    phone = input('Input a phone number: ')
    email = input('Input an email: ')
    bday = input('Input a bday: ')
    phonebook.add(name, Card(phone, email, bday))
    print('New contact added')
    unsaved_changes = True
# removing a contact
if ARGS.phonebook_action == 'remove':
    print('Deleting a contact')
    name = input('Input a name: ')
    res = phonebook.remove(name)
    if res:
        print(f'{name} removed successfully')
        unsaved_changes = True
    else:
        print(f'{name} not found')
# searching for a contact
if ARGS.phonebook_action == 'search':
    print('Searching for a contact')
    name = input('Input a name: ')
    print(phonebook.search(name))
if unsaved_changes:
    with open('data.txt', 'wb') as f:
        pickle.dump(phonebook, f, protocol=3)
