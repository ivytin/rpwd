#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import os

import utils
from template.interpreter import BaseInterpreter
from utils import Color
from utils import Printer


class Interpreter(BaseInterpreter):
    def __init__(self):
        super(Interpreter, self).__init__()
        Printer().start()

        self.version = '0.01'
        self.banner = """.______        ______    __    __  .___________. _______ .______      .______   ____    __    ____ .__   __.
|   _  \      /  __  \  |  |  |  | |           ||   ____||   _  \     |   _  \  \   \  /  \  /   / |  \ |  |
|  |_)  |    |  |  |  | |  |  |  | `---|  |----`|  |__   |  |_)  |    |  |_)  |  \   \/    \/   /  |   \|  |
|      /     |  |  |  | |  |  |  |     |  |     |   __|  |      /     |   ___/    \            /   |  . `  |
|  |\  \----.|  `--'  | |  `--'  |     |  |     |  |____ |  |\  \----.|  |         \    /\    /    |  |\   |
| _| `._____| \______/   \______/      |__|     |_______|| _| `._____|| _|          \__/  \__/     |__| \__|
                                                {RouterPwn}
                                              author: arvin
                                          Email: ivytin@gmail.com
                                              Version: {version}
""".format(version=self.version, RouterPwn=Color.RED + 'RouterPwn' + Color.ENDC)
        self.help_info = """Commands:
    help                        Print this help menu
    use <modules>                Select a modules for usage
    exec <shell command> <args> Execute a command in a shell
    exit                        Exit RouterSploit"""

        self.modules = utils.index_modules()
        self.main_modules_dirs = [module for module in os.listdir(utils.MODULES_DIR) if not module.startswith("__")]

    def postloop(self):
        utils.print_warning('Bye!')
        utils.printer_queue.join()

    def cmdloop(self, intro=None):
        utils.print_info(self.banner)
        utils.printer_queue.join()
        super(Interpreter, self).cmdloop()

    def do_use(self, module_path, *arg):
        module_path = utils.pythonize_path(module_path)
        module_path = '.'.join(('modules', module_path))
        try:
            current_module = utils.import_exploit(module_path)()
        except Exception as err:
            utils.print_failed(err)
            utils.printer_queue.join()

    def complete_use(self, text, line, begidx, endidx):
        module_line = line.partition(' ')[2]
        if module_line:
            igon = len(module_line) - len(text)
            return [s[igon:] for s in self.modules if s.startswith(module_line)]
        else:
            return self.main_modules_dirs

    def do_show(self, args):
        print(self.modules)

    def do_exit(self, args):
        return True

    def help_show(self):
        pass

    def help_exit(self):
        utils.print_help('Exit script')
        utils.printer_queue.join()


class ExploitInterpreter(BaseInterpreter):
    pass
