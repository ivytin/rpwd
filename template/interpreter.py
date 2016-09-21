#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import cmd
import utils
import collections
from utils import Color
from exceptions import BadHostInfoException


Target = collections.namedtuple('Target', 'host port')


class Task(object):
    def __init__(self):
        self.__targets = []
        self.__timeout = 3
        self.__threads = 8

    def add(self, host_infos):
        total = 0
        for host_info in host_infos:
            try:
                host, port = host_info.split(':')[0], host_info.split(':')[1]
                if utils.valid_host(host) and utils.valid_port(port):
                    self.__targets.append(Target(host=host, port=int(port)))
                    total += 1
            except IndexError:
                pass

        utils.print_info('Total {} hosts added'.format(total))

    def timeout(self, timeout):
        if utils.valid_timeout(timeout):
            self.__timeout = int(timeout)
        else:
            raise BadHostInfoException('bad timeout number: {}'.format(timeout))

    def file(self, path):
        # TODO read hosts info file
        pass

    def threads(self, threads):
        if utils.valid_threads(threads):
            self.__threads = int(threads)

    def show(self):
        utils.print_info("Target info: {}\n"
                         "Threads: {}\n"
                         "Timeout: {}"
                         .format(self.__targets, self.__threads, self.__timeout))

    def get_targets(self):
        return self.__targets

    def get_threads(self):
        return self.__threads

    def get_timeout(self):
        return self.__timeout

# class Target(object):
#     def __init__(self):
#         self.__host = None
#         self.__port = '80'
#         self.__timeout = 3
#         self.__hosts = []
#
#     def host(self, host):
#         if utils.valid_ip(host):
#             self.__host = host
#         else:
#             raise BadHostInfoException('bad IP address: {}'.format(host))
#
#     def port(self, port):
#         if utils.valid_port(port):
#             self.__port = port
#         else:
#             raise BadHostInfoException('bad port number: {}'.format(port))
#
#     def timeout(self, timeout):
#         if utils.valid_timeout(timeout):
#             self.__timeout = int(timeout)
#         else:
#             raise BadHostInfoException('bad timeout number: {}'.format(timeout))
#
#     def get_host(self):
#         return self.__host
#
#     def get_port(self):
#         return self.__port
#
#     def get_timeout(self):
#         return self.__timeout
#
#     def show(self, *arg):
#         utils.print_info("Target info: \n"
#                          "IP: {}\tPort: {}"
#                          .format(self.__host, self.__port))


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