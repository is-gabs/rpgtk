import abc


class Entity(abc.ABC):
    @abc.abstractmethod
    def to_dict(self):
        raise NotImplementedError

    @classmethod
    @abc.abstractclassmethod
    def from_dict(cls, payload):
        raise NotImplementedError
