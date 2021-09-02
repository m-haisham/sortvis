from queue import Queue
from threading import Thread

from .algorithms import Algorithm
from .delta import ListDelta

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

        # bind callback
        self.algorithm.array.callback = self.put

        # shows whether the algorithm has run to completion
        self.done = False

    def put(self, accessed, written, array_copy):
        # this function is primarily run by the thread created
        # as such there will only be one access to algorithm.array
        # so no thread lock is being used
        self.queue.put(ListDelta(accessed, written, array_copy))

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
            delta: ListDelta = self.queue.get()

            self.accesses += len(delta.accesses)
            self.writes += len(delta.writes)

            yield delta.access_changes, delta.write_changes, delta.snapshot

