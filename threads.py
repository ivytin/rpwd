#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'arvin'
import queue
import threading

import time

import utils
from exceptions import StopThreadPoolExecutor

data_queue = queue.Queue()
data_producing = threading.Event()

class WorkerThead(threading.Thread):
    def __init__(self, name):
        super(WorkerThead, self).__init__(name=name)
        self.name = name

    def run(self):
        while not data_queue.empty() or data_producing.is_set():
            try:
                task = data_queue.get(block=False)
            except queue.Empty:
                continue

            target = task[0]
            args = task[1:]
            try:
                target(*args)
            except StopThreadPoolExecutor:
                utils.print_info()
                utils.print_status("Waiting for already scheduled jobs to finish...")
                data_queue.queue.clear()
            finally:
                data_queue.task_done()


class ThreadPoolExecutor(object):
    def __init__(self, threads):
        self.threads = threads
        self.workers = None
        self.start_worker = []
        # self.monitor_work = None
        self.start_time = None

    def __enter__(self):
        workers = []
        data_producing.set()
        for worker_id in range(self.threads):
            worker = WorkerThead("worker-{}".format(worker_id))
            workers.append(worker)

        self.workers = iter(workers)
        self.start_time = time.time()
        return self

    def __exit__(self, *args):
        data_producing.clear()
        try:
            while not data_queue.empty():
                time.sleep(1)
        except KeyboardInterrupt:
            utils.print_info()
            utils.print_status("Waiting for already scheduled jobs to finish...")
            data_queue.queue.clear()
        finally:
            for worker in self.start_worker:
                worker.join()
            data_queue.unfinished_tasks = 0

        utils.print_status('Elapsed time: ', time.time() - self.start_time, 'seconds')

    def submit(self, *args):
        try:
            worker = next(self.workers)
        except StopIteration:
            pass
        else:
            worker.start()
            self.start_worker.append(worker)

        data_queue.put(args)
