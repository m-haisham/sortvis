from queue import Queue
from threading import Thread

from visualizer.sorting.algorithms.algorithm import Algorithm


class AlgorithmController(Thread):
    accesses: int = 0
    writes: int = 0

    def __init__(self, algorithm: Algorithm, maxsize=0):
        # thread controls
        super(AlgorithmController, self).__init__()
        self.setDaemon(True)
        self.setName(algorithm.__class__.__name__.split(".")[0])

        self.queue = Queue(maxsize=maxsize)

        self.algorithm = algorithm
        self.algorithm.array.callback = self.put

        # shows whether the algorithm has run to completion
        self.done = False

    def put(self, accessed, written):
        self.queue.put((accessed, written, self.algorithm.array[:]))

    def run(self):
        print(f'[Thread:{self.getName()}] Started')

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
            item = self.queue.get()

            self.accesses += len(item[0])
            self.writes += len(item[1])

            yield set(item[0] + item[1]), item[2]

