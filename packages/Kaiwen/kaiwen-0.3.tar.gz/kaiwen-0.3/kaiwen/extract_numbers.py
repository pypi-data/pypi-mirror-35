#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 10:34
# @Author  : kaiwen Xue
# @File    : extract_numbers.py
# @Software: PyCharm
import re


def extract_numbers(string, type=None, ext=None):

    if type is None and ext is None:
        return re.sub('\D', '', string)

    elif type == list and ext is None:
        return re.findall('\d', string)

    elif type is None and ext == reversed:
        return re.sub('\d', '', string)

    elif type == list and ext == reversed:
        num_list = re.findall('\d', string)
        num_length = len(num_list)
        count =0
        result_list = []

        for nums in num_list:
            count += 1
            temp_list = string.split(nums)

            if count != num_length:
                result_list.append(temp_list[0].strip())

                if len(temp_list) == 2:
                    string = temp_list[1]
                else:
                    string = nums.join(temp_list[1:])

            else:
                result_list.append(temp_list[0].strip())
                result_list.append(temp_list[1].strip())

        while '' in result_list:
            result_list.remove('')

        return result_list

    elif type is not None and type != list:
        raise Exception(type, 'is an invalid attribute!')

    elif ext is not None and ext != reversed:
        raise Exception(ext, 'is an invalid attribute!')
