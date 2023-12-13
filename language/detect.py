import re
import json

# ensure there's at least 1 lower case char
EN_PAT = re.compile(r'[a-zA-Z]*[a-z][a-zA-Z]*', re.MULTILINE)
ZH_PAT = re.compile(r'[\u4e00-\u9fff]+', re.MULTILINE)

EN_DEL_WORDS = ["3d", "3D", "Facebook", "Instagram", "Twitter", "iPhone", "iPad", "iPod", "TikTok", "Tik Tok", "YouTube", "Google", "OpenAI", "TensorFlow", "PyTorch", "Statista", "QR Code", "Podcast", "Wi-Fi", "PayPal", "Apple Pay", "Google Pay", "Adblock", "Ghostery", "DeepMind", "AlphaGo", "Hashtag", "Mac"]

def count(text: str = "", lang: str = "en"):
    if lang == "en":
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
        en_words = EN_PAT.findall(text)
        # notice that single upper case chars will be filtered out, such as I, A, etc
        return len(en_words)
    elif lang == "zh":
        zh_words = ZH_PAT.findall(text)
        return sum(map(len, ZH_PAT.findall(text)))
    else:
        raise NotImplementedError(f"lang '{lang}' is not implemented")

def detect(text: str = "", lang: str = "en"):
    return count(text, lang)


