#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/11/18 19:45
# @Author  : Kaiwen Xue
# @File    : word_filter.py
# @Software: PyCharm


def word_filter(string):
    file = open('source/SensitiveWords.txt')
    words = file.readlines()
    filter_list = [word.strip() for word in words]

    for i in filter_list:
        number_of_star = len(i)
        string = string.replace(i, '*' * number_of_star)

    return string
