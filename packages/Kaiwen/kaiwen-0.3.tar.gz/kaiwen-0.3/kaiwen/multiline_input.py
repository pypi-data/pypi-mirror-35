#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/1/18 21:30
# @Author  : kaiwen Xue
# @File    : multiline_input.py
# @Software: PyCharm


def multiline_input():
    lines = []
    words = input("Please input multiple lines, start a new line and input ':q' to save and quit:")

    while words != ':q':

        lines.append(words)
        words = input()

    return lines