#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import cmd
import queue
import utils
from utils import Color

scan_result_queue = queue.Queue()


class BaseInterpreter(cmd.Cmd):
    def __init__(self):
        super(BaseInterpreter, self).__init__()
        self.prompt_hostname = 'rtp'
        self.prompt_module = ''
        self.help_info = ''
        self.sub_opt = None

    def generate_prompt(self):
        if self.prompt_module != '':
            self.prompt = (Color.UNDERL + '{host}' + Color.ENDC + '('
                           + Color.RED + '{modules}' + Color.ENDC + ')' + ' > ') \
                .format(host=self.prompt_hostname, modules=self.prompt_module)
        else:
            self.prompt = (Color.UNDERL + '{host}' + Color.ENDC + ' > ') \
                .format(host=self.prompt_hostname)

    def cmdloop(self, intro=None):
        self.generate_prompt()
        while True:
            try:
                super(BaseInterpreter, self).cmdloop()
                break
            except KeyboardInterrupt:
                utils.print_warning('^C')

    def default(self, line):
        utils.print_failed('*** Unknown command: {command}'.format(command=line))

    def do_help(self, args):
        if not args:
            utils.print_info(self.help_info)
        else:
            super(BaseInterpreter, self).do_help(args)

    def emptyline(self):
        pass
