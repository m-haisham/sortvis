
class Algorithm:
    def __init__(self, array: list):
        self.array = array

    def iterative_sort(self):
        """
        yield changed array after change
        """
        raise NotImplementedError

    def sort(self):
        """
        sort the whole array
        """
        raise NotImplementedError
