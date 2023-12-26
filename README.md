# language-detection
Detect if a language exists in the texts. Notice that some special words in English (DNA, COVID, YouTube, etc) will not be detected.

## Install
```bash
pip install git+https://github.com/andyh0913/language-detection.git
```

## Usage
```python
from langdetect import detect
result = detect("測試") # {'zh': 2, 'en': 0}
result = detect("Hello, world!") # {'zh': 0, 'en': 2}
result = detect("我是American.") # {'zh': 2, 'en': 1}
result = detect("DNA說明了你動機跟理由", lang="zh") # {'zh': 9}
result = detect("DNA說明了你動機跟理由", lang="en") # {'en': 0}
```
