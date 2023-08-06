#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 14:17
# @Author  : kaiwen Xue
# @File    : english_format_checker.py
# @Software: PyCharm


def english_format_checker(string):
    symbol_list = [',', '.', ';', ')', ']', '}', '?']
    end_symbol_list = ['.', '?']
    not_end_symbol_list = [i for i in symbol_list if i not in end_symbol_list]
    single_list = list(string)

    # Capitalize the first word of string
    single_list[0] = single_list[0].upper()
    single_list_length = len(single_list)
    symbol_index_list = [i for i, x in enumerate(single_list) if x in symbol_list]
    index_count = 0
    add_blank_index_list = []

    # Add blank after symbols.
    if single_list_length - 1 in symbol_index_list:
        symbol_index_list.remove(single_list_length - 1)

    for indexes in symbol_index_list:

        if single_list[indexes+1] != ' ':
            add_blank_index_list.append(indexes)

    for indexes in add_blank_index_list:
        index_count += 1
        single_list.insert(indexes + index_count, ' ')

    # Capitalize the first words after end symbols.
    single_list_length = len(single_list)
    end_symbol_index_list = [i for i, x in enumerate(single_list) if x in end_symbol_list]

    if single_list_length - 1 in end_symbol_index_list:
        end_symbol_index_list.remove(single_list_length - 1)

    for indexes in end_symbol_index_list:
        single_list[indexes+2] = single_list[indexes+2].upper()

    string = ''.join(single_list)

    # Lower the first characters after not end symbols
    single_list_length = len(single_list)
    end_symbol_index_list = [i for i, x in enumerate(single_list) if x in not_end_symbol_list]

    if single_list_length - 1 in end_symbol_index_list:
        end_symbol_index_list.remove(single_list_length - 1)

    for indexes in end_symbol_index_list:
        single_list[indexes + 2] = single_list[indexes + 2].lower()

    result_string = ''.join(single_list)

    return result_string
