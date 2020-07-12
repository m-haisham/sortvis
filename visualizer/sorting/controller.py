import time
from queue import Queue
from threading import Thread

from .algorithm import Algorithm


class AlgorithmController(Thread):
    def __init__(self, algorithm: Algorithm, maxsize=0):
        # thread controls
        super(AlgorithmController, self).__init__()
        self.setDaemon(True)
        self.setName(algorithm.__class__.__name__.split(".")[0])

        self.algorithm = algorithm

        # shows whether the algorithm has run to completion
        self.done = False

        self.queue = Queue(maxsize=maxsize)

    def run(self):
        print(f'[Thread:{self.getName()}] Started')

        for array in self.algorithm.iterative_sort():
            self.queue.put(array[:])

        self.done = True
        print(f'[Thread:{self.getName()}] Done')

    @property
    def iterator(self):
        """
        iterates through array timeline

        :yield: new array points
        """
        while not self.done or not self.queue.empty():
            yield self.queue.get()

