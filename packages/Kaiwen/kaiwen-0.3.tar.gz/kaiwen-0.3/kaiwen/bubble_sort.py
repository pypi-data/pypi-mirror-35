#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/1/18 21:53
# @Author  : kaiwen Xue
# @File    : bubble_sort.py
# @Software: PyCharm


def bubble_sort(foo):
    n = len(foo)
    count = 0

    for j in range(n - 1):

        for i in range(0, n - 1 - j):

            if foo[i] > foo[i + 1]:
                foo[i], foo[i + 1] = foo[i + 1], foo[i]
                count += 1

    return foo, count
