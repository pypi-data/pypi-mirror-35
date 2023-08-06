#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 11:27
# @Author  : kaiwen Xue
# @File    : merge_dicts.py
# @Software: PyCharm


def merge_dicts(*args):
    n = len(args)
    i = 0
    result = {}

    while i < n:

        for key, value in args[i].items():
            result[key] = value + result.get(key, 0)

        i += 1

    return result
