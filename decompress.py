# !/usr/bin/python
# coding=utf-8
import re
from compress import symbols

def decompress(compressed_content):

    _content = compressed_content 
    for key in symbols:
        aux = _content.replace(symbols[key], key)
        _content = aux

    return _content
    
# SOLUTION #2
# def decompress(compressed_content):

#     symbols = {value:key for key, value in symbols.items()}
#     words = re.split('(\W)', compressed_content)
#     new_words = []
#     for w in words:
#         if w in symbols:
#             new_words.append(symbols[w])
#         else:
#             new_words.append(w)
    
#     return ''.join(new_words)