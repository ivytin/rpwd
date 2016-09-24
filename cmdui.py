#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import os

import utils
from exceptions import ModuleImportException
from template.interpreter import BaseInterpreter
from utils import Color


class CmdInterpreter(BaseInterpreter):
    def __init__(self):
        super(CmdInterpreter, self).__init__()

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

        self.main_modules_dirs = [module for module in os.listdir(utils.MODULES_DIR) if not module.startswith("__")]

    def postloop(self):
        utils.print_warning('Bye!')

    def cmdloop(self, intro=None):
        utils.print_info(self.banner)
        super(CmdInterpreter, self).cmdloop()

    def do_use(self, module_path, *arg):
        module_path = utils.pythonize_path(module_path)
        module_path = '.'.join(('modules', module_path, '__interpreter__'))
        try:
            utils.import_module(module_path, 'Interpreter')()
        except ModuleImportException as err:
            utils.print_failed(err)

    def complete_use(self, text, *args, **kwargs):
            return [module for module in self.main_modules_dirs if module.startswith(text)]

    def do_show(self, args):
        for module in self.main_modules_dirs:
            utils.print_info(module, end='\t')
        utils.print_info('')

    def do_exit(self, args):
        return True

    def help_show(self):
        pass

    def help_exit(self):
        utils.print_help('Exit script')


class ExploitInterpreter(BaseInterpreter):
    pass
