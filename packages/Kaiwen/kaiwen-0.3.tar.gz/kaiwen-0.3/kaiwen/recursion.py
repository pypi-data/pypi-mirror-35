#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 17:52
# @Author  : kaiwen Xue
# @File    : recursion.py
# @Software: PyCharm
from random import randint


def sum_it(foo):

    if len(foo) == 1:
        return foo[0]
    else:
        return foo.pop() + sum_it(foo)


def quick_sort(foo):

    if len(foo) < 2:
        return foo
    else:
        r = randint(0, len(foo)-1)
        pivot = foo.pop(r)
        smaller = [i for i in foo if i < pivot]
        larger = [i for i in foo if i > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(larger)