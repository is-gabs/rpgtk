from typing import List, Optional

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
        cards (List[Card]|None): The initial set of cards.
    '''
    def __init__(self, cards: Optional[List[Card]] = None):
        if not cards:
            cards = [Card(value=value) for value in DEFAULT_CARDS_VALUES]

        self.cards = cards
