#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import utils
import threads
from template.interpreter import BaseInterpreter, Target
from exceptions import BadHostInfoException, ModuleImportException


class Interpreter(BaseInterpreter):
    def __init__(self):
        super(Interpreter, self).__init__()
        self.prompt_module = 'Scanner'
        self.module = None
        self.modules = utils.index_modules(modules_directory='/'.join((utils.MODULES_DIR, 'scanner/')))
        self.sub_opt = {'set': ['host', 'port', 'output'],
                        'show': ['host', 'port', 'output', 'all'], }
        self.target = Target()
        self.cmdloop()

    def init_exploit(self):
        pass

    def change_prompt(self, scanner):
        self.prompt_module = scanner.prompt
        self.generate_prompt()

    def do_load(self, scanner_name):
        module_path = utils.pythonize_path(scanner_name)
        module_path = '.'.join(('modules.scanner', module_path))
        try:
            self.module = utils.import_module(module_path, 'Scanner')
        except ModuleImportException as err:
            utils.print_failed(err)
            utils.printer_queue.join()
        else:
            self.change_prompt(self.module)

    def complete_load(self, text, line, *args, **kwargs):
        if text:
            available_modules = [s for s in self.modules if s.startswith(text)]

            def split_modules(available_module):
                head, _, tail = available_module[len(text):].partition('.')
                if head:
                    return text + head
                if not head and not tail:
                    return
                else:
                    next_head, _, _ = tail.partition('.')
                    return text + '.' + next_head

            return list(map(split_modules, available_modules))
        else:
            return self.modules

    def do_set(self, args):
        try:
            sub_opt, arg = args.split(' ')[0], args.split(' ')[1]
            if sub_opt not in self.sub_opt['set']:
                raise BadHostInfoException()
        except IndexError:
            utils.print_failed("Error during setting '{}'\n"
                               "Not enough arguments\n"
                               "Use <tab> key multiple times for completion.".format(args))
            utils.printer_queue.join()
            return
        except BadHostInfoException as err:
            utils.print_failed("Error during setting '{}'\n"
                               "Use <tab> key multiple times for completion.".format(args))
            utils.printer_queue.join()
            return
        try:
            self.target.__getattribute__(sub_opt)(arg)
        except BadHostInfoException as err:
            utils.print_failed("Error during setting '{}'\n"
                               "{}.\n"
                               "Please check the arguments input.".format(sub_opt, err))
            utils.printer_queue.join()

    def complete_set(self, text, *args):
        return self.auto_complete(text, 'set')

    def do_show(self, arg):
        self.target.show()
        utils.print_info('Output info:')
        utils.printer_queue.join()

    def do_run(self, arg):
        utils.print_info('checking if module loaded')
        if not self.check_module_loaded():
            utils.print_failed('checking module failed\n'
                               'Please make sure you have already choose one module')
            return

        utils.print_info('checking targets info')
        if not self.check_target_arg():
            utils.print_failed('checking targets info failed\n'
                               'Please make sure you input info target info')
            return
        else:
            utils.print_success('passing checking...')

        with threads.ThreadPoolExecutor(3) as executor:
            executor.submit(self.target_func, self.target)

        utils.print_info()

        utils.print_success('all tasks finished...')
        utils.printer_queue.join()

    def do_back(self, arg):
        return True

    def complete_show(self, text, *args):
        return self.auto_complete(text, 'show')

    def auto_complete(self, text, opt):
        if text:
            return [' '.join((attr, '')) for attr in self.sub_opt[opt] if attr.startswith(text)]
        else:
            return self.sub_opt[opt]

    def check_target_arg(self):
        if self.target.get_host():
            return True
        else:
            return False

    def check_module_loaded(self):
        if self.module:
            return True
        else:
            return False

    def target_func(self, target):
        self.module.scan(target.get_host(), target.get_port(), target.get_timeout())
