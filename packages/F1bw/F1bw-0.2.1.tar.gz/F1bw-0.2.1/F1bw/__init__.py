#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# Copyright (C) 2018, Michael Chigaev.
#
# F1bw is free software; you can redistribute it and/or modify
# it under the terms of the 3-Clause BSD License; see LICENSE.txt
# file for more details.

import sys

import click

@click.command()
@click.option("-f", is_flag=True, help="Transforms forward a string.")
@click.option("-i", is_flag=True, help="Does the inverse on a string.")
@click.option("-r", default=-1, help="Looks for repeats and highlights them by lowercasing them after transformation.")
@click.option("-rb", default=-1, help="Looks for repeats and highlights them by lowercasing them before transformation.")
@click.option("--endchr", default="%", help="The end character, only used for the inverse operation. The default character is %", required=False)
@click.argument("string", default="")
def main(f, i, r, rb, endchr, string):
    """
    Transforms forward or does the inverse on a string, and if specified, highlights repeats by lowercasing them after running the transform function.
    :param f: f is a boolean which tells the function to run the forward function.
    
    :param i: i is a boolean which tells the function to run the inverse function.

    :param r: number input that tells the program to look for repeats greater than or equal to the length specified, and highlight them by lowercasing them.
    
    :param rb: number input that tells the program to look for repeats greater than or equal to the equal number before transforming the string, and highlights them be lowercasing letters.

    :param endchr: the endchr is the end character that is supplied to determine the original string when running the inverse

    :arg string: the string is the text that is supplied to either transform or have the inverse run on it.
    """
    if rb != -1:
        print("Repeats before trasformation: " + rep(string, rb))
    if not f and not i:
        f = not f
    if string == "":
        string = sys.stdin.read().strip()
        if len(string) == 0:
            print("The string must be specified either through execution or through stdin")
            sys.exit(1)
    if f and i:
        string = string.strip()
        if endchr not in string:
            string = string + "%"
        fw = forward(string)
        if r > -1:
            fw = rep(fw, r)
        print(fw)
        inv = inverse(fw, endchr)
        print(inv.rstrip("%"))
        sys.exit(0)
    if f:
        out = forward(string)
        if r > -1:
            out = rep(out, r)
        print(out)
        sys.exit(0)
    elif i:
        if endchr not in string:
            print("The end character must be in the string that is to have the inverse applied to it. The default end character is %. See --help")
            sys.exit(1)
        out = inverse(string, endchr)
        if r > -1:
            out = rep(out, r)
        print(out)
        sys.exit(0)
    else:
        print("A transformation must be specified, see --help.")
        sys.exit(1)


from .cli import *

if __name__ == "__main__":
	main()
