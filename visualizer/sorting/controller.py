from queue import Queue
from threading import Thread

from visualizer.sorting.algorithms.algorithm import Algorithm


class AlgorithmController(Thread):
    def __init__(self, algorithm: Algorithm, maxsize=0):
        # thread controls
        super(AlgorithmController, self).__init__()
        self.setDaemon(True)
        self.setName(algorithm.__class__.__name__.split(".")[0])

        self.queue = Queue(maxsize=maxsize)

        self.algorithm = algorithm

        # shows whether the algorithm has run to completion
        self.done = False

    def put(self, indexes):
        self.queue.put((indexes, self.algorithm.array[:]))

    def run(self):
        print(f'[Thread:{self.getName()}] Started')

        self.algorithm.array.callback = self.put

        self.algorithm.sort()
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

