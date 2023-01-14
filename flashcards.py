# -*- coding: utf-8 -*-

"""
This is an object based flashcard program.

Object: Flashcard
Each Flashcard object will have the following attributes:
    - question
    - answer
    - subset (to designate subject matter, subset of subject matter)
    - number (used for place in set, randomization,
              arbitrary unless order matters)
    - status (pass, maybe, fail)
    
Each Flashcard object will have the following methods:
    - flip_card (reveals answer, asks user to input score)
    

Object: Deck
Each Deck object will have the following attributes:
    - name
    - total_collection (collection of Card objects)
    - sets (list of all sets)
    - pass_collection (collection of Card objects set to pass)
    - maybe_collection (collection of Card objects set to maybe)
    - fail_collection (collection of Card objects set to fail)
    - set_collection (collection of Card objects belonging to a single subset)
    
Each Deck object will have the following methods:
    - add_to_deck (adds Card or other Deck to this Deck)
    - deck_to_df (converts the Deck into a DataFrame)
    - total_cards (number of total cards)
    - get_sets (returns a list of all unique sets in the deck)
    - total_sets (number of total sets)
    - name_sets (display what sets are in collection, and number of cards)
    - score_collection (assign cards to proper scoring collection)
    - quiz (flips through specified set or collection)
    - single_set (fills set_collection with a single specified subset)
    - shuffle_collection (shuffles a given collection)
    - delete_set (deletes specified set(s) out of total_collection)
    - reorder_collection (orders the cards by set and then increasing numerical order)
    - delete_card (deletes a single specified card out of total_collection)
    - reset_deck (empties all of the list attributes)
    - import_csv (fills a Deck object with Card objects made from csv file rows)
    - export_csv (exports a Deck object as a csv file)
    

The intermediate plan is to make the idea work and look into the application
transfer process at a later time.
"""

import numpy as np
import pandas as pd
import random
import sympy as sp
from sympy import symbols
from sympy import init_printing
x, y, z, t, s, u, v = sp.symbols('x y z t s u v')

class Flashcard:
    def __init__(self, question, answer, subset, number):
        self.question = question
        self.answer = answer
        self.subset = subset
        self.number = number
        self.status = 'fail'
        
    """
    Methods:
        - flip_card (reveals answer, asks user to input score)
    """
    
    """
    flip_card: this method will show the answer of a flashcard, and will ask the user
    to assign the card either a 'pass', 'fail', or 'maybe' score.
    """
    def flip_card(self):
        print(f'Answer: {self.answer}')
        designation = 'dummy'
        while designation.lower()[0] not in ['p', 'f', 'm']:
            designation = input('Designate card as (p)ass, (f)ail, or (m)aybe: ')
            print('')
            
        if designation.lower() == 'p':
            self.status = 'pass'
        elif designation.lower() == 'f':
            self.status = 'fail'
        else:
            self.status = 'maybe'

class Deck:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.total_collection = []
        self.sets = []
        self.pass_collection = []
        self.maybe_collection = []
        self.fail_collection = []
        self.set_collection = []
        
    """
    - add_to_deck (adds Card or other Deck to this Deck)
    - deck_to_df (converts the Deck into a DataFrame)
    - total_cards (number of total cards)
    - get_sets (returns a list of all unique sets in the deck)
    - total_sets (number of total sets)
    - name_sets (display what sets are in collection, and number of cards)
    - score_collection (assign cards to proper scoring collection)
    - quiz (flips through specified set or collection)
    - single_set (fills set_collection with a single specified subset)
    - shuffle_collection (shuffles a given collection)
    - delete_set (deletes specified set(s) out of total_collection)
    - reorder_collection (orders the cards by set and then increasing numerical order)
    - delete_card (deletes a single specified card out of total_collection)
    - reset_deck (empties all of the list attributes)
    """
    
    """
    add_to_deck: this method will add either a Card or Deck object to the specified
    Deck object.
    """
    def add_to_deck(self, addition):
        if type(addition) == Flashcard:
            self.total_collection.append(addition)
        elif type(addition) == Deck:
            [self.total_collection.append(card) for card in addition.total_collection]
        else:
            print('Cannot complete the addition, please use a Card or Deck type object.')
    
    """
    deck_to_df: this method will convert a Deck object into a Pandas DataFrame,
    where each row is input from a Card object.
    """
    def deck_to_df(self):
        df = pd.DataFrame(columns = vars(self.total_collection[0]).keys())
        for number, card in enumerate(self.total_collection):
            df.loc[number] = vars(card).values()
        return df
    
    """
    total_cards: this method will return the number of Card objects in the Deck object.
    """
    def total_cards(self):
        return len(self.total_collection)
    
    """
    get_sets: this method will return a unique list of the subsets in the Deck object.
    """
    def get_sets(self):
        df = self.deck_to_df()
        self.sets = list(df.subset.value_counts().index)
    
    """
    total_sets: this method will return the number of unique subsets in the Deck object.
    """
    def total_sets(self):
        self.get_sets()
        return len(self.sets)    
    
    """
    name_sets: this method will return a Pandas DataFrame printout of each unique
    subject and its respective number of Card objects.
    """
    def name_sets(self):
        df = self.deck_to_df()
        return df.subset.value_counts()
    
    """
    score_collection: this method will fill the three different score lists.
    """
    def score_collection(self):
        for card in self.total_collection:
            if card.status == 'pass':
                self.pass_collection.append(card)
            elif card.status == 'maybe':
                self.maybe_collection.append(card)
            else:
                self.fail_collection.append(card)
    
    """
    quiz: this method will allow the user to pick if they want to be tested on the entire 
    deck (total_collection), or if they want to be tested on one of the three score containers.
    """
    def quiz(self, score_specific = False):
        self.score_collection()
        quiz_set = []
        
        # choose which collection to be quizzed on (default is all)
        if score_specific == False:
            quiz_set = self.total_collection
        else:
            quiz_score = 'dummy'
            while quiz_score.lower()[0] not in ['p', 'f', 'm']:
                quiz_score = input('Choose from the following scores: (p)ass, (f)ail, or (m)aybe')
            
            if quiz_score.lower() == 'p':
                quiz_set = self.pass_collection
            elif quiz_score.lower() == 'f':
                quiz_set = self.fail_collection
            else:
                quiz_set = self.maybe_collection
                
        # get quizzed
        for card in quiz_set:
            print(f'Question: {card.question}')
            flip_or_quit = input('(f)lip or (q)uit?: ')
            print('')
            if flip_or_quit.lower()[0] == 'f':
                card.flip_card()
            else:
                break
        self.score_collection()
        
    """
    single_set: this method will fill the set_collection list with a specified subset.
    """
    def single_set(self, collection):
        self.set_collection = [card for card in self.total_collection if card.subset in collection]
    
    """
    shuffle_collection: this method will shuffle the entire Deck (total_collection)
    """
    def shuffle_collection(self):
        random.shuffle(self.total_collection)
    
    """
    delete_set: this method will delete a specified subset within in the Deck.
    """
    def delete_set(self, subset):
        self.get_sets()
        while subset in self.sets:
            for card in self.total_collection:
                if subset == card.subset:
                    self.total_collection.remove(card)
            self.get_sets()
    
    """
    reorder_collection: this method will put the Deck back in order by subset and number.
    """
    def reorder_collection(self):
        self.get_sets()
        for collection in self.sets:
            self.single_set([collection])
            self.delete_set(collection)
            sorted_set = []
            for card in self.set_collection:
                sorted_set.insert(card.number - 1, card)
            for card in sorted_set:
                self.add_to_deck(card)
    """
    delete_card: this method will delete a single card, specified by subset and number.
    """
    def delete_card(self, subset, number):
        for card in self.total_collection:
            if card.subset == subset and card.number == number:
                self.total_collection.remove(card)
        self.reorder_collection()
    
    """
    reset_deck: this method will set all list attributes of a Deck to empty
    """
    def reset_deck(self):
        self.total_collection = []
        self.sets = []
        self.pass_collection = []
        self.maybe_collection = []
        self.fail_collection = []
        self.set_collection = []
    
    """
    import_csv: this method will populate a Deck object with each row of a csv
    file being treated as a Card object.
    """
    def import_csv(self, name, path = '', reset_deck = False):
        if reset_deck != False:
            self.reset_deck()
            
        if path == '':
            df = pd.read_csv(f'{name}.csv')
        else:
            df = pd.read_csv(f'{path}/{name}.csv')
            
        for row in df.index:
            card = Flashcard(df.iloc[row].question, df.iloc[row].answer, df.iloc[row].subset, df.iloc[row].number)
            self.add_to_deck(card)
    
    """
    export_csv: this method will turn a Deck expressed as a Pandas DataFrame
    into a csv file.
    """
    def export_csv(self, name, path = ''):
        df = self.deck_to_df()
        if path == '':
            df.to_csv(f'{name}.csv', index = False)
        else:
            df.to_csv(f'{path}/{name}.csv', index = False)