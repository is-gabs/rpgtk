from rpgtk.items.base import Entity


class Item(Entity):
    '''
    The representation of a Item.

    Args:
        name (str): The item's name
        description (str|None): A short description
    '''
    def __init__(
        self, name,
        description: str = '',
        value: int = None,
        weight: int = None
    ):
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight

    def to_dict(self) -> dict:
        return dict(
            name=self.name,
            description=self.description,
            value=self.value,
            weight=self.weight
        )

    @classmethod
    def from_dict(cls, payload: dict):
        return cls(**payload)
