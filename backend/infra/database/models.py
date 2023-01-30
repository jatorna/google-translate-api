from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
import datetime

from infra.database.database import Base


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String)
    source_language = Column(String)
    target_language = Column(String)
    data = Column(JSONB)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    __table_args__ = (UniqueConstraint('word', 'source_language', 'target_language', name='_word_sl_tl_uc'),
                      )