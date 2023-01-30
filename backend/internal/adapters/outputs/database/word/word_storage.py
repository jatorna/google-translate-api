"""Word Storage adapter"""
from internal.core.entities import schemas
from internal.core.ports.word.word_ports import WordStorageOutputPort
from infra.database import models
from infra.database.database import get_db
from sqlalchemy.sql import text
from sqlalchemy import desc, asc


# pylint: disable=R0913
class WordStorageOutputAdapter(WordStorageOutputPort):
    """Word Storage Output Adapter Class"""

    def create_word(self, word: schemas.WordIn):
        """Create Word Function"""
        database = next(get_db())
        db_word = models.Word(word=word.word,
                              source_language=word.source_language,
                              target_language=word.target_language,
                              data=word.data)
        database.add(db_word)
        database.commit()
        database.refresh(db_word)
        return db_word

    def delete_word(self, word: str, source_lang: schemas.Language, target_lang: schemas.Language):
        """Delete Word Function"""
        database = next(get_db())
        db_word = database.query(models.Word).filter(
            models.Word.word == word,
            models.Word.source_language == source_lang.value,
            models.Word.target_language == target_lang.value).first()
        if db_word is None:
            return None

        database.delete(db_word)
        database.commit()
        return db_word

    def get_word(self, word: str, source_lang: schemas.Language, target_lang: schemas.Language):
        """Get Word Function"""
        database = next(get_db())
        return database.query(models.Word).filter(
            models.Word.word == word,
            models.Word.source_language == source_lang.value,
            models.Word.target_language == target_lang.value).first()

    def get_words(self, source_lang: schemas.Language, target_lang: schemas.Language,
                  order_by: schemas.OrderBy,
                  offset: int, limit: int,
                  order_direction: schemas.OrderDirection,
                  text_filter, extended: bool):
        """Get Words Function"""
        database = next(get_db())

        if order_direction == schemas.OrderDirection.DESC:
            db_data = database.query(models.Word).filter(
                models.Word.word.like('%' + text_filter + '%'),
                models.Word.source_language == source_lang.value,
                models.Word.target_language == target_lang.value). \
                order_by(desc(text(order_by))).offset(offset).limit(limit).all()
            db_data_more_items = database.query(models.Word).filter(
                models.Word.word.like('%' + text_filter + '%'),
                models.Word.source_language == source_lang.value,
                models.Word.target_language == target_lang.value). \
                order_by(desc(text(order_by))).offset(offset + limit).limit(1).all()
        else:
            db_data = database.query(models.Word).filter(
                models.Word.word.like('%' + text_filter + '%'),
                models.Word.source_language == source_lang.value,
                models.Word.target_language == target_lang.value).order_by(
                asc(text(order_by))).offset(offset).limit(limit).all()
            db_data_more_items = database.query(models.Word).filter(
                models.Word.word.like('%' + text_filter + '%'),
                models.Word.source_language == source_lang.value,
                models.Word.target_language == target_lang.value). \
                order_by(asc(text(order_by))).offset(offset + limit).limit(1).all()

        if extended:
            output = schemas.WordListExtended
            output.sl = source_lang
            output.tl = target_lang
            output.limit = limit
            output.offset = offset
            output.words = []
            output.more_items = len(db_data_more_items) > 0
            for item in db_data:
                output.words.append(item)
        else:
            output = schemas.WordList
            output.sl = source_lang
            output.tl = target_lang
            output.limit = limit
            output.offset = offset
            output.words = []
            output.more_items = len(db_data_more_items) > 0
            for item in db_data:
                output.words.append(item.word)
        return output
