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