from enum import Enum
from random import shuffle
from typing import Any, List, Optional, Union

from rpgtk.cards.constants import DEFAULT_CARD_COVER, DEFAULT_CARDS_VALUES


class Positions(Enum):
    BEGIN = 'begin'
    MIDDLE = 'middle'
    END = 'end'


class Card:
    '''
    The representation of a Card.

    Args:
        value (any): The card content.
        is_flippled (bool): If the card content is accessible.
        cover (str): The card cover.
    '''
    def __init__(
        self, value: Any,
        is_flipped: bool = False,
        cover: str = DEFAULT_CARD_COVER
    ):
        self.value = value
        self.is_flipped = is_flipped
        self.cover = cover

    def __repr__(self) -> str:
        return str(self.value if not self.is_flipped else self.cover)

    def flip(self):
        self.is_flipped = not self.is_flipped


class Deck:
    '''
    The collective of cards.

    Args:
        cards (Optional[List[Card]]): The initial set of cards.
        default (bool): Create a deck with default set of cards.
    '''
    def __init__(
        self,
        cards: Optional[List[Card]] = None,
        default: bool = False
    ):
        if cards is None:
            cards = list()

        if default:
            cards = [Card(value=value) for value in DEFAULT_CARDS_VALUES]

        self.cards = cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index: int):
        return self.cards[index]

    def draw(self) -> Union[Card, None]:
        try:
            return self.cards.pop()
        except IndexError:
            return None

    def shuffle(self) -> None:
        shuffle(self.cards)

    def pack(self, card: Card, position: Positions = Positions.END):
        index = None
        if position == Positions.MIDDLE:
            size = len(self)
            index = int((size if size > 0 else 1)/2)
        elif position == Positions.END:
            index = len(self)
        else:
            index = 0

        self.cards.insert(index, card)
