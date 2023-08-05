#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 14:35
# @Author  : Kaiwen Xue
# @File    : word_cloud.py
# @Software: PyCharm
from wordcloud import WordCloud
import jieba
from imageio import imread
import matplotlib.pyplot as plt


def wordcloud(textfile_name, output_pic_type):
    comment_text = open(textfile_name+'.txt', 'r').read()
    cut_text = " ".join(jieba.cut(comment_text))

    if output_pic_type == 'person':
        color_mask = imread('source/person.jpg')
    elif output_pic_type == 'round':
        color_mask = imread('source/round.pgn')
    else:
        return 'Wrong pic type! Expect person or round.'

    cloud = WordCloud(
        font_path="source/PingFang Regular.ttf",
        background_color='white',
        mask=color_mask,
        max_words=1000,
        max_font_size=150
    )
    word_cloud = cloud.generate(cut_text)
    word_cloud.to_file("wc_output.jpg")

    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()

