#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 10:33
# @Author  : kaiwen Xue
# @File    : extract_chinese_characters.py
# @Software: PyCharm
import re


def extract_chinese_characters(string, type=None, ext=None):

    if type is None and ext is None:
        return re.sub(r'[^\u4e00-\u9fa5]', '', string)

    elif type == list and ext is None:
        return re.findall(r'[\u4e00-\u9fa5]', string)

    elif type is None and ext == reversed:
        return re.sub(r'[\u4e00-\u9fa5]', '', string)

    elif type == list and ext == reversed:
        characters_list = re.findall(r'[\u4e00-\u9fa5]', string)
        characters_length = len(characters_list)
        count = 0
        result_list = []

        for characters in characters_list:
            count += 1
            temp_list = string.split(characters)

            if count != characters_length:
                result_list.append(temp_list[0].strip())

                if len(temp_list) == 2:
                    string = temp_list[1]
                else:
                    string = characters.join(temp_list[1:])

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