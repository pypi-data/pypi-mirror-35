# -*- coding: utf-8 -*-
#
# Copyright (C) 2018, Michael Chigaev.
#
# F1bw is free software; you can redistribute it and/or modify
# it under the terms of the 3-Clause BSD License; see LICENSE.txt
# file for more details.

#Note: The code from the radix_sort function to the burrows_wheeler_custom is not my code. It is also buggy, so it will be replaced with better and faster code.

from functools import partial

def radix_sort(values, key, step=0):
    """
    Performs a radix sort.
    :param the values to sort.
    
    :param key: The key to use.
   
    :param step: The current step. Default is 0.
    """
    if len(values) < 2:
        for value in values:
            yield value
        return
    bins = {}
    for value in values:
        bins.setdefault(key(value, step), []).append(value)
    for k in sorted(bins.keys()):
        for r in radix_sort(bins[k], key, step + 1):
            yield r


def bw_key(text, value, step):
    """
    Generates a key for a character in text
    :param text: the text to have a key generated from.
    
    :param value: The value which is used to determine the character, in addition to the step.
    
    :param step: The step, used in the radix sort.
    """
    return text[(value + step) % len(text)]


def burroughs_wheeler_custom(text):
    """
    Performs the transformation.
    :param: text the text to be transformed.
    """
    return ''.join(text[i - 1] for i in radix_sort(range(len(text)), partial(bw_key, text)))


def forward(inp):
    """
    Transforms forward the string, ignore case.
    :param inp: the text to be transformed with ignored case.
    """
    inp = inp.upper()
    inp = burroughs_wheeler_custom(inp)
    return inp


def inverse(inp, endchr):
    """
    Performs the inverse of the transformation.
    :param inp: the text to have the inverse applied to it.
    
    :param endchr: the end character that is used to figure out the original string.
    """
    out = []
    x = 0
    while x < len(inp):
        out.append("")
        x += 1
    x = 0
    while x < len(inp):
        y = 0
        while y < len(inp):
            out[y] = inp[y] + out[y]
            y += 1
        out.sort(key=str.upper)
        x += 1
    for z in out:
        if z[len(z) - 1] == endchr:
            out = z
    return out


def rep(text, num):
    """
    Finds repeats greater than or equal to a certain length, and lowercases them.
    
    :param text: The text to be searched.

    :param num: The length of the repeat.
    """
    text = text.upper()
    x = 0
    while x < len(text) - 1:
        if text[x] == text[x + 1]:
            h = x
            while True:
                if not x < len(text) - 1 or not text[x] == text[x + 1]:
                    break
                x += 1
            if abs(x + 1 - h) >= num:
                text = text[0:h] + text[h:x + 1].lower() + text[x + 1:len(text)] 
        x += 1
    if num <= 1:
        text = text.lower()
    return text
