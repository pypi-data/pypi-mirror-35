#!/usr/bin/env python3
# coding: utf-8

#############################################
# File Name: pzm.py
# Author: nosoyyo
# Mail: oyyoson@gmail.com
# Created Time:  2018-08-29 17:23:50
#############################################
__author__ = 'nosoyyo'
__version__ = '0.0.3'

import os
import fire
import time
import numpy as np
from PIL import Image

from .doc import __help__
from .hub import ImageHub


class PinZimu():

    def sniff() -> list:
        '''
        sniff the shits out
        only support the recursive depth of 1 for the moment
        so the pics will either be in cwd or subs

        :return: a list of `str` or a list of list of `str`
        '''
        # `os.walk` returns a list of tuples
        # with first item always the name of the dir, a `str`
        # then a list of sub-directories
        # then a list of non-dir contents in cwd, usually files
        walk = list(os.walk(os.getcwd()))
        result = []

        def getPic(haslet: tuple) -> list:
            result = [haslet[0]]
            result.append(
                [f for f in haslet[2] if f.split('.')[-1] in ImageHub.legal])
            return result

        cwd = getPic(walk[0])
        result.append(cwd)
        del walk[0]
        if walk:
            subd = [getPic(i) for i in walk if getPic(i)[1]]
            result.extend(subd)

        print(f'\nfound {sum([len(i[1]) for i in result])} pics \
        in {len(result)} dirs.\n')
        return [i for i in result if i]

    def splice(folder: list,
               cwd: str,
               start=None,
               height=None,
               end=None) -> np.ndarray:
        '''
        '''

        os.chdir(folder[0])

        pics = folder[1]
        pics.sort()
        pic_height = Image.open(pics[0]).height
        start = -int(pic_height * .2) or start
        subtitle_height = int(pic_height * .1) or height
        end = start + subtitle_height or end

        thumbnail = ImageHub(Image.open(pics[0]))._ndarray[:end]
        subtitles = [ImageHub(Image.open(pic))._ndarray[start:end]
                     for pic in pics[1:]]

        try:
            for i in range(len(subtitles)-1):
                thumbnail = np.concatenate((thumbnail, subtitles[i]))
        except Exception:
            print(Exception)

        suffix = f".{pics[0].split('.')[-1]}"
        ImageHub.save(thumbnail, os.getcwd().split('/')[-1]+suffix)

        if os.getcwd != cwd:
            os.chdir(cwd)

        return f'{len(pics)} -> 1 done.'


def main(*args, **kw):
    '''
    :param: <None> 默认自动处理当前目录下全部子目录，默认字幕位置`-20%`, 高度`10%`
    :param: <folder name> 处理当前目录下某个子目录

    :param: `start` 图片从下往上开始截取的相对位置，例如`-200`
    :param: `end` 截到哪为止，例如`-100`
    :param: `height` 截取多高

    :TODO: `start` 和 `end` 如果为正，则按绝对定位截取；否则相对
    '''
    cwd = os.getcwd()
    materials = PinZimu.sniff()

    if not materials:
        return '\nno picture found. \nbye!\n'

    if not any([args, kw]):
        # TODO automatically get everything done
        for folder in materials:
            PinZimu.splice(folder, cwd)
    # 简单的帮助文档
    elif 'help' in args or '?' in args:
        return __help__


def entry():
    fire.Fire(main)


if __name__ == '__main__':
    time0 = time.time()
    fire.Fire(main)
    time1 = time.time()
    print(f':2.{time1 - time0} seconds.')
