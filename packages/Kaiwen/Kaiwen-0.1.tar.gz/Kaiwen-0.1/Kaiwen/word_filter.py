#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/11/18 19:45
# @Author  : Kaiwen Xue
# @File    : word_filter.py
# @Software: PyCharm


def get_user_input():
    user_input = input('Please input something: ')
    return user_input


def word_replace():
    user_input = get_user_input()
    filter_list = ['fuck', 'shit', 'stupid', 'kill']

    for i in filter_list:
        number_of_star = len(i)
        user_input = user_input.replace(i, '*' * number_of_star)

    return user_input


