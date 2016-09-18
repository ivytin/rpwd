#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import importlib
import os
import queue
import threading
import sys
import collections
import modules as rtp_modules

PrintResource = collections.namedtuple("PrintResource", ['content', 'sep', 'end', 'file'])
printer_queue = queue.Queue()
MODULES_DIR = rtp_modules.__path__[0]

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


def list_dirs(path):
    dirs = {name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))}
    if "__pycache__" in dirs:
        dirs.remove("__pycache__")
    if ".cache" in dirs:
        dirs.remove(".cache")
    return dirs


def index_modules(modules_directory=MODULES_DIR):
    """ Return list of all modules """

    modules = []
    for root, dirs, files in os.walk(modules_directory):
        _, package, root = root.rpartition('routerpwn/modules/'.replace('/', os.sep))
        root = root.replace(os.sep, '.')
        files = filter(lambda x: not x.startswith("__") and x.endswith('.py'), files)
        modules.extend(map(lambda x: '.'.join((root, os.path.splitext(x)[0])), files))

    return modules


def import_exploit(path):
    """ Import exploit module

    :param path: absolute path to exploit e.g. routersploit.modules.exploits.asus.pass_bypass
    :return: exploit module or error
    """
    try:
        module = importlib.import_module(path)
        return getattr(module, 'Exploit')
    except (ImportError, AttributeError, KeyError) as err:
        raise Exception(
            "Error during loading '{}'\n"
            "Error: {}\n"
            "It should be valid path to the module. "
            "Use <tab> key multiple times for completion.".format(humanize_path(path), err)
        )


def humanize_path(path):
    """ Replace python dotted path to directory-like one.

    ex. foo.bar.baz -> foo/bar/baz

    :param path: path to humanize
    :return: humanized path

    """
    return path.replace('.', '/')


def pythonize_path(path):
    """ Replace argument to valid python dotted notation.

    ex. foo/bar/baz -> foo.bar.baz
    """
    return path.replace('/', '.')


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
    __print('[+]', *args, color=Color.GREEN, **kwargs)
    # __print(*args, **kwargs)


def print_failed(*args, **kwargs):
    __print('[-]', *args, color=Color.RED, **kwargs)
    # __print(*args, **kwargs)


def print_warning(*args, **kwargs):
    __print(*args, color=Color.YELLOW, **kwargs)


def print_help(*args, **kwargs):
    __print(*args, color=Color.PURPLE, **kwargs)


def print_info(*args, **kwargs):
    __print(*args, **kwargs)


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
