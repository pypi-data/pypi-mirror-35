# -*- coding: utf-8 -*-

try:
    print(u"\u2660", u"\u2665", u"\u2666", u"\u2663")
    has_unicode = True
except UnicodeEncodeError:
    has_unicode = False
