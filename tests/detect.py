#!/usr/bin/env python
from langdetect import detect

if __name__ == "__main__":
  text = "Hello world, 我叫做 Wilson"
  
  result_zh = detect(text, lang='zh')
  print('zh:', result_zh)

  result_all = detect(text)
  print('all:', result_all)