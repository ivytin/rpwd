#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import cmd
import utils
from utils import Color
from exceptions import BadHostInfoException


class Target(object):
    def __init__(self):
        self.__host = None
        self.__port = '80'
        self.__timeout = 3

    def host(self, host):
        if utils.valid_ip(host):
            self.__host = host
        else:
            raise BadHostInfoException('bad IP address: {}'.format(host))

    def port(self, port):
        if utils.valid_port(port):
            self.__port = port
        else:
            raise BadHostInfoException('bad port number: {}'.format(port))

    def timeout(self, timeout):
        if utils.valid_timeout(timeout):
            self.__timeout = int(timeout)
        else:
            raise BadHostInfoException('bad timeout number: {}'.format(timeout))

    def get_host(self):
        return self.__host

    def get_port(self):
        return self.__port

    def get_timeout(self):
        return self.__timeout

    def show(self, *arg):
        utils.print_info("Target info: \n"
                         "IP: {}\tPort: {}"
                         .format(self.__host, self.__port))


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
                utils.printer_queue.join()

    def default(self, line):
        utils.print_failed('*** Unknown command: {command}'.format(command=line))
        # must wait util printer thread finishs print_failed() call,
        # or the output sequence will be disorganized
        utils.printer_queue.join()

    def do_help(self, args):
        if not args:
            utils.print_info(self.help_info)
            utils.printer_queue.join()
        else:
            super(BaseInterpreter, self).do_help(args)