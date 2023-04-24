import ssl

import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import collections


# Cleans text (removes any punctuation)
def CleanText(text):
    text = str(text)
    forbidden = [r'\n', r'.', r'?', r'!', r'(', r')']
    for i in forbidden:
        text.replace(i, '')
    return text

# returns count of a word from a page
def ReturnCount(url):
    r = requests.get(url, allow_redirects=False, verify=ssl.CERT_NONE)
    soup = BeautifulSoup(r.content, 'lxml')
    words = ''.join([t for t in soup.body.find_all(text=True)])
    words = CleanText(words.lower())
    words = words.split()
    counter = collections.Counter(words)
    common_words = counter.most_common(20)
    count_data_frame = pd.DataFrame(common_words,
                             columns=['words', 'count'])
    return  count_data_frame


ReturnCount('https://www.youtube.com/watch?v=P2pSnGEcssQ')