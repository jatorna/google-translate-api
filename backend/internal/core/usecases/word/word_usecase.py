from internal.core.entities import schemas
from internal.core.ports.word.word_ports import WordStorageOutputPort, GoogleTranslateExtendedApiOutputPort


class WordUseCase:
    db_adapter: WordStorageOutputPort
    google_translate_extended_api_adapter: GoogleTranslateExtendedApiOutputPort

    def __init__(self, db_adapter, google_translate_extended_api_adapter):
        self.db_adapter = db_adapter
        self.google_translate_extended_api_adapter = google_translate_extended_api_adapter

    def get_word(self, word: str, sl: schemas.Language, tl: schemas.Language):
        db_word = self.db_adapter.get_word(word, sl, tl)
        if db_word is not None:
            return db_word

        word_data = self.google_translate_extended_api_adapter.get_word_data(word, sl, tl)

        if word_data is None:
            return None

        word = schemas.WordIn
        word.word = word_data['word']
        del word_data['word']
        word.data = word_data
        word.source_language = sl
        word.target_language = tl
        db_word = self.db_adapter.create_word(word)
        return db_word

    def get_words(self, sl: schemas.Language, tl: schemas.Language, order_by: schemas.OrderBy, offset: int, limit: int,
                  order_direction: schemas.OrderDirection,
                  filter, extended: bool):
        return self.db_adapter.get_words(sl, tl, order_by, offset, limit, order_direction, filter, extended)

    def delete_word(self, word: str, sl: schemas.Language, tl: schemas.Language):
        return self.db_adapter.delete_word(word, sl, tl)
