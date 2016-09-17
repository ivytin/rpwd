#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import os
import queue
import threading
import sys

import collections

PrintResource = collections.namedtuple("PrintResource", ['content', 'sep', 'end', 'file'])

printer_queue = queue.Queue()


def identify_os():
    if os.name == "nt":
        operating_system = "windows"
    elif os.name == "posix":
        operating_system = "posix"
    else:
        operating_system = "unknown"
    return operating_system


if identify_os() == 'posix':

    class Color:
        BLUE = '\033[94m'
        GREEN = '\033[32m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BOLD = '\033[1m'
        UNDERL = '\033[4m'
        ENDC = '\033[0m'
else:
    class Color:
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BOLD = ''
        UNDERL = ''
        ENDC = ''


def __print(*args, **kwargs):
    color = kwargs.get('color', None)
    file = kwargs.get('file', sys.stdout)
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    if color:
        msg = color + sep.join("%s" % arg for arg in args) + Color.ENDC
        printer_queue.put(PrintResource(content=msg, sep=sep, end=end, file=file))
    else:
        msg = sep.join("%s" % arg for arg in args)
        printer_queue.put(PrintResource(content=msg, sep=sep, end=end, file=file))


def print_success(*args, **kwargs):
    __print(*args, color=Color.GREEN, **kwargs)


def print_failed(*args, **kwargs):
    __print(*args, color=Color.RED, **kwargs)


def print_warning(*args, **kwargs):
    __print(*args, color=Color.YELLOW, **kwargs)


def print_help(*args, **kwargs):
    __print(*args, color=Color.PURPLE, **kwargs)


def print_info(*args, **kwargs):
    __print(*args, color=Color.BLUE, **kwargs)


class Printer(threading.Thread):
    def __init__(self):
        super(Printer, self).__init__()
        self.daemon = True

    def run(self):
        while True:
            content, sep, end, file = printer_queue.get()
            # print(repr(content),repr(sep), repr(end), repr(file))
            # print('-----------')
            print(content, sep=sep, end=end, file=file)
            printer_queue.task_done()
