import time


class FrameRate:
    def __init__(self, limit: int = None):
        self.limit = limit

        self.target_delta = 1 / self.limit
        self.t0 = time.time()

    def update(self):
        """
        :return: framerate
        """
        t1 = time.time()
        delta = t1 - self.t0

        # reset
        self.t0 = t1

        # framerate limiter
        # if self.limit is not None:
        #
        #     # time to react average amount
        #     wait = self.target_delta - delta
        #
        #     # if framerate higher
        #     if wait > 0:
        #         time.sleep(wait)

        return 1 / delta
