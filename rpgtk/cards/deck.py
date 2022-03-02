from random import shuffle
from typing import List, Optional, Union

from rpgtk.cards.constants import DEFAULT_CARD_COVER, DEFAULT_CARDS_VALUES


class Card:
    '''
    The representation of a Card.

    Args:
        value (str): The card content.
        is_flippled (bool): If the card content is accessible.
        cover (str): The card cover.
    '''
    def __init__(
        self, value: str,
        is_flipped: bool = False,
        cover: str = DEFAULT_CARD_COVER
    ):
        self.value = value
        self.is_flipped = is_flipped
        self.cover = cover

    def __repr__(self) -> str:
        return self.value if not self.is_flipped else self.cover


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
