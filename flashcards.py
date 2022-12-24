# -*- coding: utf-8 -*-

"""
This is a flashcard based object program.

Object: Flashcard
Each Flashcard object will have the following attributes:
    - question
    - answer
    - set (to designate subject matter, subset of subject matter)
    - number (used for place in set, randomization,
              arbitrary unless order matters)
    - status (pass, maybe, fail)
Each Flashcard object will have the following methods:
    - flip_card
    - alter_status
    - alter_question
    - alter_answer
    - alter_set
    - alter_number
    

Object: Deck
Each Deck object will have the following attributes:
    - name
    - total_collection (collection of Card objects)
    - sets (list of all sets)
    - pass_collection (collection of Card objects set to pass)
    - maybe_collection (collection of Card objects set to maybe)
    - fail_collection (collection of Card objects set to fail)
    - misc_collection (collection of Card objects set to miscellaneous)?
    
Each Deck object will have the following methods:
    - total_cards (number of total cards, number of total cards)
    - name_sets (display what sets are in collection, and number of cards)
    - shuffle_collection (shuffles a given collection)
    - reorder_collection (orders the cards by set and then increasing numerical order)
    - add_to_deck (adds Card or other Deck to this Deck)
    - quiz (flips through specified set or collection)
    - reset_collection (resets specified collection)
    - alter_collection (manually alter specified collection)
    - delete_card (deletes a single specified card out of total_collection)
    - delete_set (deletes specified set(s) out of total_collection)
    

The intermediate plan is to make the idea work and look into the application
transfer process at a later time.

The ultimate plan is to replace paper flashcards in an application that can be
accessed by mobile devices, with the goal of replacing endless scrolling with
a session of flashcarding.
"""

class Flashcard:
    def __init__(self, question, answer, subset, number):
        self.question = question
        self.answer = answer
        self.subset = subset
        self.number = number
        self.status = 'fail'
        
    """
    - ask_question
    - flip_card
    - alter_status
    - alter_question
    - alter_answer
    - alter_subset
    - alter_number
    
    Is it redundant to have any of the functions besides flip_card?
    """
    def ask_question(self):
        print(self.question)
    
    def flip_card(self):
        print(self.answer)
        designation = 'dummy'
        while designation.lower()[0] not in ['p', 'f', 'm']:
            designation = input('Designate card as (p)ass, (f)ail, or (m)aybe')
        
        if designation.lower() == 'p':
            self.status = 'pass'
        elif designation.lower() == 'f':
            self.status = 'fail'
        else:
            self.status = 'maybe'
    
    def alter_status(self, new_status):
        self.status = new_status
        
    def alter_question(self, new_question):
        self.status = new_status 
        
    def alter_answer(self, new_answer):
        self.status = new_answer 
        
    def alter_set(self, new_subset):
        self.status = new_subset 
        
    def alter_number(self, new_number):
        self.status = new_number