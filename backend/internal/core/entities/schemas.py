"""Schemas module"""
import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel


# pylint: disable=R0903
class WordIn(BaseModel):
    """WordIn schema"""
    word: str
    source_language: str
    target_language: str
    data: dict


class Word(WordIn):
    """Word schema"""
    id: int
    created_date: datetime.datetime

    class Config:
        """Config class"""
        orm_mode = True


class WordList(BaseModel):
    """WordList schema"""
    sl: str
    tl: str
    words: List[str | Word]
    more_items: bool
    offset: int
    limit: int

    class Config:
        """Config class"""
        orm_mode = True


class WordListExtended(BaseModel):
    """WordListExtended schema"""
    sl: str
    tl: str
    words: List[Word]
    more_items: bool
    offset: int
    limit: int

    class Config:
        """Config class"""
        orm_mode = True


class ErrorMessage(BaseModel):
    """ErrorMessage schema"""
    error: str


class OrderDirection(str, Enum):
    """OrderDirection enum"""
    ASC = "asc"
    DESC = "desc"


class OrderBy(str, Enum):
    """OrderBy enum"""
    ID = "id"
    CREATED_DATE = "created_date"


class Language(str, Enum):
    """Language enum"""
    AF = 'af'
    SQ = 'sq'
    AM = 'am'
    AR = 'ar'
    HY = 'hy'
    AZ = 'az'
    EU = 'eu'
    BE = 'be'
    BN = 'bn'
    BS = 'bs'
    BG = 'bg'
    CA = 'ca'
    CEB = 'ceb'
    NY = 'ny'
    ZH_CN = 'zh-cn'
    ZH_TW = 'zh-tw'
    CO = 'co'
    HR = 'hr'
    CS = 'cs'
    DA = 'da'
    NL = 'nl'
    EN = 'en'
    EO = 'eo'
    ET = 'et'
    TL = 'tl'
    FI = 'fi'
    FR = 'fr'
    FY = 'fy'
    GL = 'gl'
    KA = 'ka'
    DE = 'de'
    EL = 'el'
    GU = 'gu'
    HT = 'ht'
    HA = 'ha'
    HAW = 'haw'
    IW = 'iw'
    HI = 'hi'
    HMN = 'hmn'
    HU = 'hu'
    IS = 'is'
    IG = 'ig'
    ID = 'id'
    GA = 'ga'
    IT = 'it'
    JA = 'ja'
    JW = 'jw'
    KN = 'kn'
    KK = 'kk'
    KM = 'km'
    KO = 'ko'
    KU = 'ku'
    KY = 'ky'
    LO = 'lo'
    LA = 'la'
    LV = 'lv'
    LT = 'lt'
    LB = 'lb'
    MK = 'mk'
    MG = 'mg'
    MS = 'ms'
    ML = 'ml'
    MT = 'mt'
    MI = 'mi'
    MR = 'mr'
    MN = 'mn'
    MY = 'my'
    NE = 'ne'
    NO = 'no'
    PS = 'ps'
    FA = 'fa'
    PL = 'pl'
    PT = 'pt'
    MA = 'ma'
    RO = 'ro'
    RU = 'ru'
    SM = 'sm'
    GD = 'gd'
    SR = 'sr'
    ST = 'st'
    SN = 'sn'
    SD = 'sd'
    SI = 'si'
    SK = 'sk'
    SL = 'sl'
    SO = 'so'
    ES = 'es'
    SU = 'su'
    SW = 'sw'
    SV = 'sv'
    TG = 'tg'
    TA = 'ta'
    TE = 'te'
    TH = 'th'
    TR = 'tr'
    UK = 'uk'
    UR = 'ur'
    UZ = 'uz'
    VI = 'vi'
    CY = 'cy'
    XH = 'xh'
    YI = 'yi'
    YO = 'yo'
    ZU = 'zu'
