"""Database Models"""
import datetime
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from infra.database.database import Base

# pylint: disable=R0903
class Word(Base):
    """Word Model"""

    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String)
    source_language = Column(String)
    target_language = Column(String)
    data = Column(JSONB)
    created_date = Column(DateTime,
                          default=datetime.datetime.utcnow)
    __table_args__ = (UniqueConstraint('word', 'source_language',
                                       'target_language', name='_word_sl_tl_uc'),)
