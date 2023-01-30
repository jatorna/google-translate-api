"""Word Use case"""
from internal.core.entities import schemas
from internal.core.ports.word.word_ports import \
    WordStorageOutputPort, GoogleTranslateExtendedApiOutputPort


# pylint: disable=R0913
class WordUseCase:
    """Word Use case Class"""
    db_adapter: WordStorageOutputPort
    google_translate_extended_api_adapter: GoogleTranslateExtendedApiOutputPort

    def __init__(self, db_adapter, google_translate_extended_api_adapter):
        """Init method"""
        self.db_adapter = db_adapter
        self.google_translate_extended_api_adapter = google_translate_extended_api_adapter

    def get_word(self, word: str, source_lang: schemas.Language, target_lang: schemas.Language):
        """Get word method"""
        db_word = self.db_adapter.get_word(word, source_lang, target_lang)
        if db_word is not None:
            return db_word

        word_data = self.google_translate_extended_api_adapter.get_word_data(
            word, source_lang, target_lang)

        if word_data is None:
            return None

        word = schemas.WordIn
        word.word = word_data['word']
        del word_data['word']
        word.data = word_data
        word.source_language = source_lang
        word.target_language = target_lang
        db_word = self.db_adapter.create_word(word)
        return db_word

    def get_words(self, source_lang: schemas.Language,
                  target_lang: schemas.Language, order_by: schemas.OrderBy,
                  offset: int, limit: int,
                  order_direction: schemas.OrderDirection,
                  text_filter, extended: bool):
        """Get words method"""
        return self.db_adapter.get_words(source_lang, target_lang,
                                         order_by, offset, limit, order_direction,
                                         text_filter, extended)

    def delete_word(self, word: str, source_lang: schemas.Language,
                    target_lang: schemas.Language):
        """Delete word method"""
        return self.db_adapter.delete_word(word, source_lang, target_lang)
