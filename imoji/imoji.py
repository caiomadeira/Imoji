"""
API KEY: PCoVVp1nYFhYbBImiDg9sSMhI
API KEY SECRET: iUFr4IDxupB6DDqkwP8wcReTysY7G8KYCPszi9S2BQtmAMgKE6

ACESS TOKEN: 1317291421523726342-kc5u5yJjz92cKuIesRezMlAJpifl7K
ACESS TOKEN SECRET: 5gUHmXtXYZC8yxc2QataiqcLhitVQzpVTb3ntC6yOyOKD


status id with unicode clow: 1446951831737876490
status id without any unicode: 1444946581891977218
"""

import PIL
import tweepy
import os
import unicodedata

from PIL import Image, ImageDraw, ImageOps, ImageFilter
from PIL import *

consumer_key = "PCoVVp1nYFhYbBImiDg9sSMhI"
consumer_secret = "iUFr4IDxupB6DDqkwP8wcReTysY7G8KYCPszi9S2BQtmAMgKE6"
access_token = "1317291421523726342-kc5u5yJjz92cKuIesRezMlAJpifl7K"
access_token_secret = "5gUHmXtXYZC8yxc2QataiqcLhitVQzpVTb3ntC6yOyOKD"


def get_text():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    id = 1446951831737876490
    status = api.get_status(id)
    text = status.text
    print(text)
    unic = text.encode("unicode_escape")
    print(unic)
    return unic


def get_unicode():
    unicode_in_text = get_text()
    emoji_list = []
    if isinstance(unicode_in_text, str):
        print("just string")
    elif isinstance(unicode_in_text, bytes):
        print("unicode data")
        strlist = unicode_in_text.decode("utf-8").split()
        # print(strlist)
        for u in strlist:
            if u.startswith('\\U'):
                print("Unicode founded:", u)
                if "\\U000" in u:
                    rm_prefix = u.replace("\\U000", "")
                    print("Unicode trated:", u)
                    emoji_list.append(rm_prefix)
                    return emoji_list


def search_for_emoji():
    unicode_list = get_unicode()
    print("Search unicode:", unicode_list)
    for root, dirs, files in os.walk("emojis"):
        for name in files:
            # print(name)
            try:
                for u in unicode_list:
                    unicode_img = u + ".png"
                    if name == unicode_img:
                        # print("yes")
                        print("Unicode returned sucessfully:", unicode_img)
                        return unicode_img
            except TypeError:
                return "No unicode found in list"


def unicode_action():
    status = search_for_emoji()

    if "No unicode found in list" in status:
        print("Fuck.")
        quit()
    else:
        img = Image.open(f'imoji/emojis/{status}').convert('RGBA')
        return img
