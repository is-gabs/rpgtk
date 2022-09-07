class Item:
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
