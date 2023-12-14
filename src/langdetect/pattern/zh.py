from .general import ez_count
import re

PAT = re.compile(r'[\u4e00-\u9fff]+', re.MULTILINE)

def count(text: str=""):
    return ez_count(text, PAT)