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
    

The current plan is to build these 

The ultimate plan is to replace paper flashcards in an application that can be
accessed by mobile devices, with the goal of replacing endless scrolling with
a session of flashcarding.
"""