from internal.core.entities import schemas
from internal.core.ports.word.word_ports import GoogleTranslateExtendedApiOutputPort
import subprocess
import json


class GoogleTranslateExtendedApiOutputAdapter(GoogleTranslateExtendedApiOutputPort):

    def get_word_data(self, word: schemas.WordIn, sl: schemas.Language, tl: schemas.Language):
        raw_data = subprocess.check_output(
            "node scripts/javascript/google_translate_extended_api.js " + word + " " + sl +
            " " + tl, shell=True)

        word_data = json.loads(raw_data)
        if len(word_data['translations']) == 0 and len(word_data['definitions']) == 0 and len(
                word_data['examples']) == 0 and word_data['wordTranscription'] is None:
            return None

        return word_data
