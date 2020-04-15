# !/usr/bin/python
# coding=utf-8
import re

symbols = {
    "implementation": "🤯",
    "practicality": '🤩',
    "better": '😅',
    "Although": "🥺"
}

def compress(content):

    words = re.split('(\W)', content)
    new_words = []
    for w in words:
        try:
            new_words.append(symbols[w])
        except KeyError:
            new_words.append(w)
    return ''.join(new_words)
    