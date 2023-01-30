"""Word ports module"""
import abc
from internal.core.entities import schemas


# pylint: disable=R0913
class WordStorageOutputPort(metaclass=abc.ABCMeta):
    """Word Storage Output Port Class"""

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
    def get_word(self, word: str, source_lang: schemas.Language, target_lang: schemas.Language):
        """Get word from database"""
        raise NotImplementedError

    @abc.abstractmethod
    def delete_word(self, word: str, source_lang: schemas.Language, target_lang: schemas.Language):
        """Delete word in database"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_words(self, source_lang: schemas.Language, target_lang: schemas.Language,
                  order_by: schemas.OrderBy, offset: int, limit: int,
                  order_direction: schemas.OrderDirection,
                  text_filter, extended: bool):
        """Get words from database"""
        raise NotImplementedError


class GoogleTranslateExtendedApiOutputPort(metaclass=abc.ABCMeta):
    """Google Translate Extended Api Output Port class"""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_word_data') and
                callable(subclass.get_word_data) or
                NotImplemented)

    @abc.abstractmethod
    def get_word_data(self, word: schemas.WordIn, source_lang: schemas.Language,
                      target_lang: schemas.Language):
        """Get word data from Google Translate extended API"""
        raise NotImplementedError
