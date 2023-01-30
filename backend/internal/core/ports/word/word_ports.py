import abc
from internal.core.entities import schemas


class WordStorageOutputPort(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'create_word') and
                callable(subclass.create_word) and
                hasattr(subclass, 'get_word') and
                callable(subclass.get_word) and
                hasattr(subclass, 'delete_word') and
                callable(subclass.delete_word) and
                hasattr(subclass, 'get_words') and
                callable(subclass.get_words) or
                NotImplemented)

    @abc.abstractmethod
    def create_word(self, word: schemas.WordIn):
        """Create word in database"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_word(self, word: str, sl: schemas.Language, tl: schemas.Language):
        """Get word from database"""
        raise NotImplementedError

    @abc.abstractmethod
    def delete_word(self, word: str, sl: schemas.Language, tl: schemas.Language):
        """Delete word in database"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_words(self, sl: schemas.Language, tl: schemas.Language, order_by: schemas.OrderBy, offset: int, limit: int,
                  order_direction: schemas.OrderDirection,
                  filter, extended: bool):
        """Get words from database"""
        raise NotImplementedError


class GoogleTranslateExtendedApiOutputPort(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_word_data') and
                callable(subclass.get_word_data) or
                NotImplemented)

    @abc.abstractmethod
    def get_word_data(self, word: schemas.WordIn, sl: schemas.Language, tl: schemas.Language):
        """Get word data from Google Translate extended API"""
        raise NotImplementedError
