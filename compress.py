 # !/usr/bin/python
# coding=utf-8
import re

symbols = {
#   key             :   symbols[key]
    "implementation":   "🤯",
    "practicality"  :   '🤩',
    "is better than":   '😅',
    "than"          :   '😘',
    "Although"      :   "🥺",
}

def compress(content):
    
    _content = content 
    for key in symbols:
        aux = _content.replace(key, symbols[key])
        _content = aux

    return _content

# SOlution 2
# def compress(content):
#     words = re.split('(\W)', content)
#     new_words = []
#     for w in words:
#         if w in symbols:
#             new_words.append(symbols[w])
#         else:
#             new_words.append(w)
#     return ''.join(new_words)