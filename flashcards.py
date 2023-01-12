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
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

class Flashcard:
    def __init__(self, question, answer, subset, number):
        self.question = question
        self.answer = answer
        self.subset = subset
        self.number = number
        self.status = 'fail'
        
    """
    Methods:
        - flip_card
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
    - shuffle_collection (shuffles a given collection)
    - reorder_collection (orders the cards by set and then increasing numerical order)
    - reset_collection (resets numbering on specified collection)
    - delete_card (deletes a single specified card out of total_collection)
    - delete_set (deletes specified set(s) out of total_collection)
    """
    
    def add_to_deck(self, addition):
        if type(addition) == Flashcard:
            self.total_collection.append(addition)
        elif type(addition) == Deck:
            [self.total_collection.append(card) for card in addition.total_collection]
        else:
            print('Cannot complete the addition, please use a Card or Deck type object.')
            
    def deck_to_df(self):
        df = pd.DataFrame(columns = vars(self.total_collection[0]).keys())
        for number, card in enumerate(self.total_collection):
            df.loc[number] = vars(card).values()
            
        return df
        
    def total_cards(self):
        return len(self.total_collection)
    
    def get_sets(self):
        df = self.deck_to_df()
        self.sets = list(df.subset.value_counts().index)
    
    def total_sets(self):
        self.get_sets()
        return len(self.sets)    
    
    def name_sets(self):
        df = self.deck_to_df()
        return df.subset.value_counts()
    
    def score_collection(self):
        for card in self.total_collection:
            if card.status == 'pass':
                self.pass_collection.append(card)
            elif card.status == 'maybe':
                self.maybe_collection.append(card)
            else:
                self.fail_collection.append(card)
    
    def quiz(self, score_specific = False):
        self.score_collection()
        quiz_set = []
        
        # choose which collection to be quizzed on
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
        
    def single_set(self, collection):
        self.set_collection = [card for card in self.total_collection if card.subset in collection]
                
    def shuffle_collection(self):
        random.shuffle(self.total_collection)
                
    def delete_set(self, subset):
        self.get_sets()
        while subset in self.sets:
            for card in self.total_collection:
                if subset == card.subset:
                    self.total_collection.remove(card)
            self.get_sets()
    
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
                
    def delete_card(self, subset, number):
        for card in self.total_collection:
            if card.subset == subset and card.number == number:
                self.total_collection.remove(card)
        self.reorder_collection()
    
    def reset_deck(self):
        self.total_collection = []
        self.sets = []
        self.pass_collection = []
        self.maybe_collection = []
        self.fail_collection = []
        self.set_collection = []
        
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
    
    def export_csv(self, name, path = ''):
        df = self.deck_to_df()
        if path == '':
            df.to_csv(f'{name}.csv', index = False)
        else:
            df.to_csv(f'{path}/{name}.csv', index = False)

    
    
    
            

card1 = Flashcard('question1', 'answer1', 'a', 1)
card2 = Flashcard('question2', 'answer2', 'a', 2)
card3 = Flashcard('question3', 'answer3', 'a', 3)
card4 = Flashcard('question4', 'answer4', 'b', 1)
card5 = Flashcard('question5', 'answer5', 'b', 2)
    
deck_a = Deck('deck_a')
deck_b = Deck('deck_b')
deck_c = Deck('deck_c')

set_a = [card1, card2, card3]
set_b = [card4, card5]

[deck_a.add_to_deck(card) for card in set_a]
[deck_b.add_to_deck(card) for card in set_b]

deck_c.add_to_deck(deck_a)
deck_c.add_to_deck(deck_b)

dc = deck_c.deck_to_df()
deck_c.shuffle_collection()
deck_c.reorder_collection()
dc = deck_c.deck_to_df()








