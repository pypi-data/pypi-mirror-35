#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 10:17
# @Author  : Kaiwen Xue
# @File    : my_re.py
# @Software: PyCharm
import re


def extract_chinese_character(string):
    return re.sub(r'[^\u4e00-\u9fa5]', '', string)


def extract_numbers(string):
    return re.sub('\D', '', string)