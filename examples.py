# -*- coding: utf-8 -*-
"""
Examples file for flashcards.py module.

1. Creating a Card object
2. flip_card
3. Creating a Deck object
4. Loading a Deck (add_to_deck)
    a. card
    b. decks
5. deck_to_df
6. total_cards
7. get_sets
8. total_sets
9. name_sets
10. score_collection
11. quiz
12. single_set
13. shuffle_collection
14. delete_set
15. reorder_collection
16. delete_card
17. reset_deck
18. csv files
    a. import_csv
    b. export_csv
19. Working with the SymPy library
"""

from flashcards import *
# 1. Creating a Card object
card = Flashcard('question 1', 'answer 1', 'set_a', 1)


# 2. flip_card
card.flip_card()
"""
Answer: answer 1
Designate card as (p)ass, (f)ail, or (m)aybe:
"""

# Note that the user would then enter in a p, f, or m


# 3. Creating a Deck object named 
deck = Deck('deck_1')


# 4. Loading a Deck (add_to_deck)
# 4a. card
deck.add_to_deck(card)

# 4b. decks
"""
let's create some arbitrary cards across multiple subsets for examples' sake.
"""

# set a will have 4 cards
a = np.arange(1, 5)
# set b will have 6 cards
b = np.arange(1,7)
# set c will have 2 cards
c = np.arange(1, 3)

# create the 3 Deck objects
deck_a = Deck('deck_a')
deck_b = Deck('deck_b')
deck_c = Deck('deck_c')

# fill the decks with their respective cards
for number, card in enumerate(a):
    card = Flashcard(f'question {number+1}_a', f'answer {number+1}_a', 'set_a', number+1)
    deck_a.add_to_deck(card)
    
for number, card in enumerate(b):
    card = Flashcard(f'question {number+1}_b', f'answer {number+1}_b', 'set_b', number+1)
    deck_a.add_to_deck(card)
    
for number, card in enumerate(c):
    card = Flashcard(f'question {number+1}_c', f'answer {number+1}_c', 'set_c', number+1)
    deck_a.add_to_deck(card)

# Returning to 4b...
# Add them one at a time OR cycle through a list which has the respective decks
deck_d = Deck('deck_d')
deck_d.add_to_deck(deck_a)

decks = [deck_b, deck_c]
[deck_d.add_to_deck(deck) for deck in decks]


# 5. deck_to_df
deck_d.deck_to_df()
"""
        question      answer subset  number status
0   question 1_a  answer 1_a  set_a       1   fail
1   question 2_a  answer 2_a  set_a       2   fail
2   question 3_a  answer 3_a  set_a       3   fail
3   question 4_a  answer 4_a  set_a       4   fail
4   question 1_b  answer 1_b  set_b       1   fail
5   question 2_b  answer 2_b  set_b       2   fail
6   question 3_b  answer 3_b  set_b       3   fail
7   question 4_b  answer 4_b  set_b       4   fail
8   question 5_b  answer 5_b  set_b       5   fail
9   question 6_b  answer 6_b  set_b       6   fail
10  question 1_c  answer 1_c  set_c       1   fail
11  question 2_c  answer 2_c  set_c       2   fail
"""

# Note that this is a great way to visualize any deck

# 6. total_cards
deck_d.total_cards()
"""
12
"""


# 7. get_sets
deck_d.get_sets()
deck_d.sets
"""
['set_b', 'set_a', 'set_c']
"""


# 8. total_sets
deck_d.total_sets()
"""
3
"""

# 9. name_sets
deck_d.name_sets()
"""
set_b    6
set_a    4
set_c    2
Name: subset, dtype: int64
"""


# 10. score_collection
deck_d.score_collection()
print(len(deck_d.pass_collection))
print(len(deck_d.maybe_collection))
print(len(deck_d.fail_collection))

"""
Note that since we haven't altered the scores (status) of the cards, every
collecton besides fail_collection will be empty

0
0
12 
""" 


# 11. quiz
# No specification results in the entire deck, 
deck_d.quiz()
"""
Question: question 1_a
(f)lip or (q)uit?:
"""
# f will reveal the answer and allow the user to change the score, q will exit

deck_d.quiz(score_specific = True)
"""
Choose from the following scores: (p)ass, (f)ail, or (m)aybe
"""

# Note that user will then choose p, f, or m to be quizzed on, respectively.


# 12. single_set
deck_d.single_set('set_a')
for card in deck_d.set_collection:
    print(card.subset)
"""
set_a
set_a
set_a
set_a
"""


# 13. shuffle_collection
"""
Recall the current structure:
    
        question      answer subset  number status
0   question 1_a  answer 1_a  set_a       1   fail
1   question 2_a  answer 2_a  set_a       2   fail
2   question 3_a  answer 3_a  set_a       3   fail
3   question 4_a  answer 4_a  set_a       4   fail
4   question 1_b  answer 1_b  set_b       1   fail
5   question 2_b  answer 2_b  set_b       2   fail
6   question 3_b  answer 3_b  set_b       3   fail
7   question 4_b  answer 4_b  set_b       4   fail
8   question 5_b  answer 5_b  set_b       5   fail
9   question 6_b  answer 6_b  set_b       6   fail
10  question 1_c  answer 1_c  set_c       1   fail
11  question 2_c  answer 2_c  set_c       2   fail    
"""

deck_d.shuffle_collection()
deck_d.deck_to_df()
"""
        question      answer subset  number status
0   question 4_a  answer 4_a  set_a       4   fail
1   question 3_a  answer 3_a  set_a       3   fail
2   question 4_b  answer 4_b  set_b       4   fail
3   question 2_a  answer 2_a  set_a       2   fail
4   question 5_b  answer 5_b  set_b       5   fail
5   question 6_b  answer 6_b  set_b       6   fail
6   question 1_b  answer 1_b  set_b       1   fail
7   question 3_b  answer 3_b  set_b       3   fail
8   question 1_c  answer 1_c  set_c       1   fail
9   question 2_c  answer 2_c  set_c       2   fail
10  question 1_a  answer 1_a  set_a       1   fail
11  question 2_b  answer 2_b  set_b       2   fail
"""


# 14. delete_set
deck_d.delete_set('set_a')
deck_d.deck_to_df()
"""
       question      answer subset  number status
0  question 4_b  answer 4_b  set_b       4   fail
1  question 5_b  answer 5_b  set_b       5   fail
2  question 6_b  answer 6_b  set_b       6   fail
3  question 1_b  answer 1_b  set_b       1   fail
4  question 3_b  answer 3_b  set_b       3   fail
5  question 1_c  answer 1_c  set_c       1   fail
6  question 2_c  answer 2_c  set_c       2   fail
7  question 2_b  answer 2_b  set_b       2   fail
"""


# 15. reorder_collection
deck_d.reorder_collection()
deck_d.deck_to_df()
"""
       question      answer subset  number status
0  question 1_b  answer 1_b  set_b       1   fail
1  question 2_b  answer 2_b  set_b       2   fail
2  question 4_b  answer 4_b  set_b       4   fail
3  question 3_b  answer 3_b  set_b       3   fail
4  question 5_b  answer 5_b  set_b       5   fail
5  question 6_b  answer 6_b  set_b       6   fail
6  question 1_c  answer 1_c  set_c       1   fail
7  question 2_c  answer 2_c  set_c       2   fail
"""


# 16. delete_card
deck_d.delete_card('set_b', 3)
deck_d.deck_to_df()


# 17. reset_deck
deck_d.reset_deck()
deck_d.total_cards()
"""
0
"""

# note that all lists are emptied, not just total_collection


# 18. csv files
# 18a. import_csv
# 18b. export_csv
"""
We'll show the csv files example out of order. Let's re-run creating deck_d,
turn it into a csv file, reset it, and then load it back in.
"""

# set a will have 4 cards
a = np.arange(1, 5)
# set b will have 6 cards
b = np.arange(1,7)
# set c will have 2 cards
c = np.arange(1, 3)

# create the 3 Deck objects
deck_a = Deck('deck_a')
deck_b = Deck('deck_b')
deck_c = Deck('deck_c')

# fill the decks with their respective cards
for number, card in enumerate(a):
    card = Flashcard(f'question {number+1}_a', f'answer {number+1}_a', 'set_a', number+1)
    deck_a.add_to_deck(card)
    
for number, card in enumerate(b):
    card = Flashcard(f'question {number+1}_b', f'answer {number+1}_b', 'set_b', number+1)
    deck_a.add_to_deck(card)
    
for number, card in enumerate(c):
    card = Flashcard(f'question {number+1}_c', f'answer {number+1}_c', 'set_c', number+1)
    deck_a.add_to_deck(card)

decks = [deck_a, deck_b, deck_c]
[deck_d.add_to_deck(deck) for deck in decks]

# 18b. export_csv
deck_d.export_csv('example')
"""
The function does have more robust pathing options. Running:
    deck.export_csv('deck', 'user/path')
Would show this in the user's directory:
    user/path/deck.csv
Similar concept about pathing options in the import option too. However, the
import function has an additional option to either reset or add to the current
deck (i.e. if we weren't to clear the deck between these steps).
"""

deck_d.reset_deck()

# 18a. import_csv
deck_d.import_csv('example')
deck_d.deck_to_df()
"""
        question      answer subset  number status
0   question 1_a  answer 1_a  set_a       1   fail
1   question 2_a  answer 2_a  set_a       2   fail
2   question 3_a  answer 3_a  set_a       3   fail
3   question 4_a  answer 4_a  set_a       4   fail
4   question 1_b  answer 1_b  set_b       1   fail
5   question 2_b  answer 2_b  set_b       2   fail
6   question 3_b  answer 3_b  set_b       3   fail
7   question 4_b  answer 4_b  set_b       4   fail
8   question 5_b  answer 5_b  set_b       5   fail
9   question 6_b  answer 6_b  set_b       6   fail
10  question 1_c  answer 1_c  set_c       1   fail
11  question 2_c  answer 2_c  set_c       2   fail
"""


# 19. Working with the SymPy Library
"""
Specifically, flashcards.py runs the following from SymPy:
    
import sympy as sp
from sympy import symbols
from sympy import init_printing

If a user is working with an IDE, or a future application, which can load SymPy
visuals then take a look at the following example.
"""

# Here, we'll create a flashcard which quizes the user on the integral of x
card = Flashcard(sp.Integral(x), sp.integrate(x), 'integrals', 1)

# Let's see what this would look like via a few different views
vars(card)
"""
{'question': Integral(x, x),
 'answer': x**2/2,
 'subset': 'integrals',
 'number': 1,
 'status': 'fail'}
"""

# Note how the text version shows up as SymPy line commands

# The following commands will show up as the actual math notation format:
card.question
card.answer

# How about in a DataFrame?
deck = Deck('calculus')
deck.add_to_deck(card)
deck.deck_to_df()
"""
         question  answer     subset  number status
0  Integral(x, x)  x**2/2  integrals       1   fail
"""

# For csv purposes, it is actually ideal the math notation doesn't form here