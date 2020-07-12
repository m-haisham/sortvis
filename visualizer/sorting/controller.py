import time
from queue import Queue
from threading import Thread

from .algorithm import Algorithm


class AlgorithmController(Thread):
    def __init__(self, algorithm: Algorithm, delay=1, maxsize=0):
        # thread controls
        super(AlgorithmController, self).__init__()
        self.setDaemon(True)

        self.algorithm = algorithm

        # time between each iteration
        self.delay = delay

        # shows whether the algorithm has run to completion
        self.done = False

        self.queue = Queue(maxsize=maxsize)

    def run(self):
        for array in self.algorithm.sort_generator():
            self.queue.put(array[:])

        self.done = True

    @property
    def iterator(self):
        """
        iterates through array timeline

        :yield: new array points
        """
        while not self.done or not self.queue.empty():
            # time.sleep(self.delay)
            yield self.queue.get()

