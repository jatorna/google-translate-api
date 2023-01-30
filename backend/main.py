"""Main module"""
import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from internal.core.entities import schemas
from internal.core.usecases.word.word_usecase import WordUseCase
from internal.adapters.outputs.database.word.word_storage import WordStorageOutputAdapter
from internal.adapters.outputs.api.googletranslate.google_translate_extended_api_adapter import \
    GoogleTranslateExtendedApiOutputAdapter
from infra.database import models
from infra.database.database import engine
from starlette.requests import Request
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

# create models in db
models.Base.metadata.create_all(bind=engine)

# init adapters and usecases
word_db_adapter = WordStorageOutputAdapter()
google_translate_extended_api_adapter = GoogleTranslateExtendedApiOutputAdapter()
word_usecase = WordUseCase(word_db_adapter, google_translate_extended_api_adapter)

# init app
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
v1 = FastAPI(title="Google Translate API", docs_url="/", version="v1.0")
v1.state.limiter = limiter
v1.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# pylint: disable=W0613
@v1.exception_handler(500)
async def internal_exception_handler(request: Request, _exc: Exception):
    """Internal Exception Handler"""
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})


# add prom middleware
@app.on_event("startup")
async def startup_event():
    """Startup Event Function"""
    Instrumentator().instrument(app).expose(app)


@v1.get("/words/{word}", response_model=schemas.Word,
        responses={404: {"model": schemas.ErrorMessage},
                   429: {"model": schemas.ErrorMessage},
                   500: {"model": schemas.ErrorMessage}})
@limiter.limit("10/minute")
def get_word(request: Request, word: str, source_lang: schemas.Language = schemas.Language.EN,
             target_lang: schemas.Language = schemas.Language.RU):
    """Get Word Endpoint"""
    word = word_usecase.get_word(word, source_lang, target_lang)
    if word is None:
        return JSONResponse(status_code=404, content={"message": "Word not found"})
    return word


@v1.delete("/words/{word}", response_model=schemas.Word,
           responses={404: {"model": schemas.ErrorMessage},
                      429: {"model": schemas.ErrorMessage},
                      500: {"model": schemas.ErrorMessage}})
@limiter.limit("10/minute")
def delete_word(request: Request, word: str, source_lang: schemas.Language = schemas.Language.EN,
                target_lang: schemas.Language = schemas.Language.RU):
    """Delete Word Endpoint"""
    word = word_usecase.delete_word(word, source_lang, target_lang)
    if word is None:
        return JSONResponse(status_code=404, content={"message": "Word not found"})
    return word


@v1.get("/words/", response_model=schemas.WordList, responses={
    429: {"model": schemas.ErrorMessage},
    500: {"model": schemas.ErrorMessage}})
@limiter.limit("10/minute")
# pylint: disable=R0913
def get_words(request: Request, source_lang: schemas.Language = schemas.Language.EN,
              target_lang: schemas.Language = schemas.Language.RU,
              offset: int = 0,
              limit: int = 10,
              order_by: schemas.OrderBy = schemas.OrderBy.ID,
              order_direction: schemas.OrderDirection = schemas.OrderDirection.ASC,
              text_filter: str = '',
              extended: bool = False):
    """Get Words Endpoint"""
    words = word_usecase.get_words(source_lang, target_lang, order_by, offset, limit,
                                   order_direction,
                                   text_filter,
                                   extended)
    return words


app.mount("/api/v1", v1)

# run server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888)
