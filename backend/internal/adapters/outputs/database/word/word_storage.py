from internal.core.entities import schemas
from infra.database import models
from sqlalchemy.sql import text
from sqlalchemy import desc, asc
from infra.database.database import get_db
from internal.core.ports.word.word_ports import WordStorageOutputPort


class WordStorageOutputAdapter(WordStorageOutputPort):

    def create_word(self, word: schemas.WordIn):
        db = next(get_db())
        db_word = models.Word(word=word.word,
                              source_language=word.source_language,
                              target_language=word.target_language,
                              data=word.data)
        db.add(db_word)
        db.commit()
        db.refresh(db_word)
        return db_word

    def delete_word(self, word: str, sl: schemas.Language, tl: schemas.Language):
        db = next(get_db())
        db_word = db.query(models.Word).filter(models.Word.word == word,
                                               models.Word.source_language == sl.value,
                                               models.Word.target_language == tl.value).first()
        if db_word is None:
            return None

        db.delete(db_word)
        db.commit()
        return db_word

    def get_word(self, word: str, sl: schemas.Language, tl: schemas.Language):
        db = next(get_db())
        return db.query(models.Word).filter(models.Word.word == word,
                                            models.Word.source_language == sl.value,
                                            models.Word.target_language == tl.value).first()

    def get_words(self, sl: schemas.Language, tl: schemas.Language, order_by: schemas.OrderBy, offset: int, limit: int,
                  order_direction: schemas.OrderDirection,
                  filter, extended: bool):
        db = next(get_db())

        if order_direction == schemas.OrderDirection.desc:
            db_data = db.query(models.Word).filter(models.Word.word.like('%' + filter + '%'),
                                                   models.Word.source_language == sl.value,
                                                   models.Word.target_language == tl.value).order_by(
                desc(text(order_by))).offset(offset). \
                limit(limit).all()
            db_data_more_items = db.query(models.Word).filter(models.Word.word.like('%' + filter + '%'),
                                                              models.Word.source_language == sl.value,
                                                              models.Word.target_language == tl.value).order_by(
                desc(text(order_by))). \
                offset(offset + limit).limit(1).all()
        else:
            db_data = db.query(models.Word).filter(models.Word.word.like('%' + filter + '%'),
                                                   models.Word.source_language == sl.value,
                                                   models.Word.target_language == tl.value).order_by(
                asc(text(order_by))).offset(offset).limit(limit).all()
            db_data_more_items = db.query(models.Word).filter(models.Word.word.like('%' + filter + '%'),
                                                              models.Word.source_language == sl.value,
                                                              models.Word.target_language == tl.value).order_by(
                asc(text(order_by))).offset(offset + limit).limit(1).all()

        if extended:
            output = schemas.WordListExtended
            output.sl = sl
            output.tl = tl
            output.limit = limit
            output.offset = offset
            output.words = []
            output.more_items = True if len(db_data_more_items) > 0 else False
            for item in db_data:
                output.words.append(item)
        else:
            output = schemas.WordList
            output.sl = sl
            output.tl = tl
            output.limit = limit
            output.offset = offset
            output.words = []
            output.more_items = True if len(db_data_more_items) > 0 else False
            for item in db_data:
                output.words.append(item.word)
        return output
