#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/11/18 19:45
# @Author  : kaiwen Xue
# @File    : word_filter.py
# @Software: PyCharm
import requests


def word_filter(string):
    url = 'https://raw.githubusercontent.com/kxue4/raw_repo/master/SensitiveWords.txt'
    words = requests.get(url).text

    filter_list = words.split('\n')

    for i in filter_list:
        number_of_star = len(i)
        string = string.replace(i, '*' * number_of_star)

    return string