# Virtual Flashcards
This project allows a user to create flashcards and decks of flashcards. It is 
meant to be a virtual replacement to physical flashcards, and features abilities
such as deck combination and shuffling.


## Table of Contents
- [Libraries Used](#libraries-used)
- [Project Motivation](#project-motivation)
- [File Descriptions](#file-descriptions)
- [Card Class Attributes](#card-class-attributes)
- [Card Class Functions](#card-class-functions)
- [Deck Class Attributes](#deck-class-attributes)
- [Deck Class Functions](#deck-class-functions)
- [Future Considerations](#future-considerations)


## Libraries Used
- NumPy
- pandas
- random
- SymPy

Notes on SymPy:
1. flashcards.py runs the following from SymPy:

```python
import sympy as sp
from sympy import symbols
from sympy import init_printing
x, y, z, t, s, u, v = sp.symbols('x y z t s u v')
```

2. flashcards.py has the following variables available for use:
- x
- y
- z
- t
- s
- u
- v

[Table of Contents](#table-of-contents)


## Project Motivation
The goal of this project was to create an object based virtual flashcards program
that could replace physical flashcards. Besides general testing, there are three
phases:

1. Create a class based program that works in an IDE
2. Create csv libraries for the desired flashcards
3. Create an application outside an IDE, with a mobile aim in mind

It was imperative to include the SymPy library, as this will personally be used heavily for
mathematical concepts. On another personal note, further motivation for developing this
into some sort of application was to swap mindless scrolling with learning during downtime.

See the 'examples.py' file for a walkthrough of the module.

[Table of Contents](#table-of-contents)


## File Descriptions
- flashcards.py: python script containing the entire flashcards module
- examples.py: python script containing examples of how to use the module
- example.csv: csv file generated if following along in 'examples.py'

[Table of Contents](#table-of-contents)


## Card Class Attributes
card = Flashcard(question, answer, subset, number)

- question
- answer
- subset: to designate subject matter, subset of subject matter
- number: used for place in set, randomization, arbitrary unless order matters
- status: pass, maybe, fail

Note that status is always initially set to "fail".

[Table of Contents](#table-of-contents)


## Card Class Functions
- flip_card: reveals answer, asks user to input score (i.e. change status)

[Table of Contents](#table-of-contents)


## Deck Class Attributes
deck = Deck(collection_name)

- collection_name: name of deck
- total_collection: list of all cards in deck
- sets: list of all sets in deck (subset attribute in Card class)
- pass_collection: list of all cards with "pass" status
- maybe_collection: list of all cards with "maybe" status
- fail_collection: list of all cards with "fail" status
- set_collection: list of cards within a specified set (subset attribute in Card class)

[Table of Contents](#table-of-contents)


## Deck Class Functions
- add_to_deck: adds card or other deck to this deck
- deck_to_df: converts the deck into a DataFrame
- total_cards: number of total cards
- get_sets: returns a list of all unique sets in the deck
- total_sets: number of total sets in deck
- name_sets: display what sets are in collection, and number of cards
- score_collection: assign cards to proper scoring collection
- quiz: flips through specified set or collection
- single_set: fills set_collection with a single specified subset
- shuffle_collection: shuffles a given collection
- delete_set: deletes specified set(s) out of total_collection
- reorder_collection: orders the cards by set and then increasing numerical order
- delete_card: deletes a single specified card out of total_collection
- reset_deck: empties all of the list attributes
- import_csv: fills a Deck object with Card objects made from csv file rows
- export_csv: exports a Deck object as a csv file

[Table of Contents](#table-of-contents)


## Future Considerations
Following the phases in [Project Motivation](#project-motivation), minor tweaks will
likely be needed in stage 1 (such as error handling measures), but focus can now be
shifted to phases 2-3.

It could be useful to add function where the user can declare their own variables
in conjunction with the SymPy module.

Naming the collection while creating a Deck object seems redundant, and may be
removed in the future.

[Table of Contents](#table-of-contents)