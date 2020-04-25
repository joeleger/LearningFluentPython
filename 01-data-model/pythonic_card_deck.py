import collections
from random import choice, randint

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# get a specific card
print('specific card')
beer_card = Card('7', 'diamonds')
print(beer_card)
print()

# find the size of the deck
print('size of the deck')
deck = FrenchDeck()
print(len(deck))
print()

# Reading specific cards by position in the deck(start)
print('specific cards by position (start)')
print(deck[0])
print()

# Reading specific cards by position in the deck(start)
print('specific cards by position (end)')
print(deck[-1])
print()

# get a random item from a sequence: random.choice.
print('random item from a sequence using random choice')
for i in range(3):
    print(choice(deck))
print()

# Our deck is iterable
for card in deck:  # doctest: +ELLIPSIS
    print(card)
print()

# Our deck is iterable and reversible
for card in reversed(deck):  # doctest: +ELLIPSIS
    print(card)
print()

# In operations (contains) builtin
print('In operations')
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)
print()

# sorting ranking cards by suit Spades, Diamnonds, Hearts, Clubs
suit_values = dict(spades=3, diamonds=2, hearts=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# spades_high, we can now list our deck in order of increasing rank:
print('list our deck in order of increasing rank')
for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
    print(card)
print()

# iterators
print('iterators')
def d6():
    return randint(1, 6)
d6_iter = iter(d6, 1)
for roll in d6_iter:
    print(roll)