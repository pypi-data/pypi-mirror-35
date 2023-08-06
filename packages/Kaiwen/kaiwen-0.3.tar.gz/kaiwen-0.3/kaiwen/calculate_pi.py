#!/usr/redundantin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/25/18 19:45
# @Author  : kaiwen Xue
# @File    : calculate_pi.py
# @Software: PyCharm
from __future__ import division


def calculate_pi(digits):
    redundant = 10 ** (digits + 10)
    x1 = redundant * 4//5
    x2 = redundant // -239
    he = x1 + x2
    digits *= 2

    for i in range(3,digits,2):
        x1 //= -25
        x2 //= -57121
        x = (x1 + x2) // i
        he += x

    pi = he * 4
    pi //= 10 ** 10
    pi = str(pi)[0] + str('.') + str(pi)[1:len(str(pi))]

    return pi