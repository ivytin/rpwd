#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import utils
from template.interpreter import BaseInterpreter


class Exploit(BaseInterpreter):
    def __init__(self):
        super(Exploit, self).__init__()
        self.prompt_module = 'Scanner'

        self.sub_opt = {'set': ['target', 'port', 'output'],
                        'show': ['target', 'port', 'output', 'all'], }

        self.cmdloop()

    def do_set(self, arg):
        pass

    def do_show(self, arg):
        pass

    def do_run(self, arg):
        utils.print_success('!!!!!!')
        utils.printer_queue.join()

    def do_back(self, arg):
        return True

    def complete_set(self, text, *args):
        return self.auto_complete(text, 'set')

    def complete_show(self, text, *args):
        return self.auto_complete(text, 'show')
