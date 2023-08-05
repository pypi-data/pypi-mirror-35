#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from jinja2 import Markup, escape
def add(x,y):
    return x+y

def division(x,y):
    return x/y

def mutiply(x,y):
    return x*y

def subtract(x,y):
    return x-y

def main():
    pass

def dypprint():
    markup = Markup("")
    print("dyp yz home")
if __name__ == '__main__':
    print("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))