#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/11/18 19:14
# @Author  : Kaiwen Xue
# @File    : generate_coupon.py
# @Software: PyCharm
import random
import string


def generate_coupon():
    coupons = []

    for n in range(200):
        generate = []

        for i in range(8):
            generate.append(random.choice(string.ascii_uppercase + string.digits))

        coupon = ''.join(generate)
        coupons.append(coupon)

    return coupons
