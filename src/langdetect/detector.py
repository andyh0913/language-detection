from typing import Union, List
import re

from .pattern.zh import count as zh_extrator
from .pattern.en import en_count as en_extrator

_factorys = None

# === Pattern Dectector ===
# seprate the two parts


LANGUAGE_EXTRACTION = {
    'zh': zh_extrator,
    'en': en_extrator,
}
SUPPORT_LANGUAGE = list(LANGUAGE_EXTRACTION.keys())
# SUPPORT_LANGUAGE_TYPE = Union(SUPPORT_LANGUAGE)
# TODO: merge two language detector under Detector.
class Detector:
    def __init__(self, lang: Union['zh', 'en']=None):
        self.lang = lang

    def detect(self, text: str=""):
        return LANGUAGE_EXTRACTION[self.lang]( text )

# === Pattern Dectector ===

# === General detect ===
def init_factory():
    global _factorys
    if _factorys == None:
        _factorys = {}
        for lang in SUPPORT_LANGUAGE:
            _factorys[lang] = Detector(lang=lang)
        
def detect(text: str="", lang: str=None, langs: list=None):
    # init all the detector
    if langs == None:
        if lang is not None:
            langs = [lang]
        else:
            langs = SUPPORT_LANGUAGE

    init_factory( )

    results = {}
    for lang in langs:
        results[lang] = _factorys[lang].detect( text )
    return results

# === General detect ===

if __name__ == "__main__":
    import json
    print('Support languages:', SUPPORT_LANGUAGE)
    print('Language special words', json.dumps(SUPPORT_LANGUAGE, indent=4))
