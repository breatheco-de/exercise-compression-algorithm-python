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
    