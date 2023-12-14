from typing import Pattern

def ez_count(text: str="", PAT: Pattern=None): # General purpose pattern extraction
    if PAT == None:
        raise ValueError('Missing regex pattern.')
    words = PAT.findall(text)
    return sum(map(len, words))