from typing import List, Optional

from rpgtk.cards.constants import DEFAULT_CARDS_VALUES


class Card:
    def __init__(self, value: str):
        self.value = value


class Deck:
    def __init__(self, cards: Optional[List[Card]] = None):
        if not cards:
            cards = [Card(value=value) for value in DEFAULT_CARDS_VALUES]

        self.cards = cards
