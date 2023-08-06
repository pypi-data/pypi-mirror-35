#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/11/18 19:14
# @Author  : kaiwen Xue
# @File    : generate_coupon.py
# @Software: PyCharm
import random
import string


def generate_coupon(num, dig_num):
    coupons = []

    for n in range(num):
        generate = []

        for i in range(dig_num):
            generate.append(random.choice(string.ascii_uppercase + string.digits))

        coupon = ''.join(generate)
        coupons.append(coupon)

    return coupons