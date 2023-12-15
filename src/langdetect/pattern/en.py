import re
from langdetect.data import loader

PAT = re.compile(r'[a-zA-Z]*[a-z][a-zA-Z]*', re.MULTILINE)
DATAPACK = None

def init_datapack():
    global DATAPACK
    if DATAPACK == None:
        # This dictionary should be under the zh or other languages. (allow to zh detect more words that should using in that language)
        DATAPACK = loader('pattern', 'en')

def en_count(text: str=""):
    init_datapack()

    EN_DEL_WORDS = DATAPACK['special_words']

    for word in EN_DEL_WORDS:
        text = re.sub(word, "", text)
    # remove text in parentheses
    text = re.sub(r"\(.*\)", "", text)
    text = re.sub(r"（.*）", "", text)
    # remove list (a. b. ...)
    text = re.sub(r"\s[A-Za-z]\.", "", text)
    # remove Roman numbers
    text = re.sub(r"\sM{0,4}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})\.", "", text)
    text = re.sub(r"\sm{0,4}(c[md]|d?c{0,3})(x[cl]|l?x{0,3})(i[xv]|v?i{0,3})\.", "", text)
    en_words = PAT.findall(text)
    # notice that single upper case chars will be filtered out, such as I, A, etc
    return len(en_words)
