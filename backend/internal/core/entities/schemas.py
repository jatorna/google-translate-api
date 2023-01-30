from pydantic import BaseModel
import datetime
from enum import Enum
from typing import List


class WordIn(BaseModel):
    word: str
    source_language: str
    target_language: str
    data: dict


class Word(WordIn):
    id: int
    created_date: datetime.datetime

    class Config:
        orm_mode = True


class WordList(BaseModel):
    sl: str
    tl: str
    words: List[str | Word]
    more_items: bool
    offset: int
    limit: int

    class Config:
        orm_mode = True


class WordListExtended(BaseModel):
    sl: str
    tl: str
    words: List[Word]
    more_items: bool
    offset: int
    limit: int

    class Config:
        orm_mode = True


class ErrorMessage(BaseModel):
    error: str


class OrderDirection(str, Enum):
    asc = "asc"
    desc = "desc"


class OrderBy(str, Enum):
    id = "id"
    created_date = "created_date"


class Language(str, Enum):
    af = 'af'
    sq = 'sq'
    am = 'am'
    ar = 'ar'
    hy = 'hy'
    az = 'az'
    eu = 'eu'
    be = 'be'
    bn = 'bn'
    bs = 'bs'
    bg = 'bg'
    ca = 'ca'
    ceb = 'ceb'
    ny = 'ny'
    zh_cn = 'zh-cn'
    zh_tw = 'zh-tw'
    co = 'co'
    hr = 'hr'
    cs = 'cs'
    da = 'da'
    nl = 'nl'
    en = 'en'
    eo = 'eo'
    et = 'et'
    tl = 'tl'
    fi = 'fi'
    fr = 'fr'
    fy = 'fy'
    gl = 'gl'
    ka = 'ka'
    de = 'de'
    el = 'el'
    gu = 'gu'
    ht = 'ht'
    ha = 'ha'
    haw = 'haw'
    iw = 'iw'
    hi = 'hi'
    hmn = 'hmn'
    hu = 'hu'
    isl = 'is'
    ig = 'ig'
    id = 'id'
    ga = 'ga'
    it = 'it'
    ja = 'ja'
    jw = 'jw'
    kn = 'kn'
    kk = 'kk'
    km = 'km'
    ko = 'ko'
    ku = 'ku'
    ky = 'ky'
    lo = 'lo'
    la = 'la'
    lv = 'lv'
    lt = 'lt'
    lb = 'lb'
    mk = 'mk'
    mg = 'mg'
    ms = 'ms'
    ml = 'ml'
    mt = 'mt'
    mi = 'mi'
    mr = 'mr'
    mn = 'mn'
    my = 'my'
    ne = 'ne'
    no = 'no'
    ps = 'ps'
    fa = 'fa'
    pl = 'pl'
    pt = 'pt'
    ma = 'ma'
    ro = 'ro'
    ru = 'ru'
    sm = 'sm'
    gd = 'gd'
    sr = 'sr'
    st = 'st'
    sn = 'sn'
    sd = 'sd'
    si = 'si'
    sk = 'sk'
    sl = 'sl'
    so = 'so'
    es = 'es'
    su = 'su'
    sw = 'sw'
    sv = 'sv'
    tg = 'tg'
    ta = 'ta'
    te = 'te'
    th = 'th'
    tr = 'tr'
    uk = 'uk'
    ur = 'ur'
    uz = 'uz'
    vi = 'vi'
    cy = 'cy'
    xh = 'xh'
    yi = 'yi'
    yo = 'yo'
    zu = 'zu'
