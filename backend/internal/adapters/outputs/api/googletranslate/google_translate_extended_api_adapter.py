"""Google Translate API adapter"""
import subprocess
import json
from internal.core.entities import schemas
from internal.core.ports.word.word_ports import GoogleTranslateExtendedApiOutputPort


# pylint: disable=R0903
class GoogleTranslateExtendedApiOutputAdapter(GoogleTranslateExtendedApiOutputPort):
    """Google Translate Extended Api Output Adapter Class"""

    def get_word_data(self, word: schemas.WordIn, source_lang: schemas.Language,
                      target_lang: schemas.Language):
        """Get word data function"""
        raw_data = subprocess.check_output(
            "node scripts/javascript/google_translate_extended_api.js " + word + " " + source_lang +
            " " + target_lang, shell=True)

        word_data = json.loads(raw_data)
        if len(word_data['translations']) == 0 and len(word_data['definitions']) == 0 and len(
                word_data['examples']) == 0 and word_data['wordTranscription'] is None:
            return None

        return word_data
