from collections import MutableSequence
from typing import List, Callable, TypeVar

_T = TypeVar('_T')


class CallbackList(MutableSequence):
    """
    callback on each change to sequence with indexes that changed
    """

    # callback(accessed_indexes, written_indexes)
    callback: Callable[[List[int], List[int]], None]

    def __init__(self, callback: Callable[[List[int], List[int]], None], li: List = None):

        # initialize callback function
        self.callback = callback

        # initialize inner list
        if li is None:
            self._inner_list = []
        else:
            self._inner_list = li

    #########
    #  new  #
    #########
    def swap(self, i1: int, i2: int):
        """
        swap value of index one with other

        it is recommended to use this for swaps
        """
        self._inner_list[i1], self._inner_list[i2] = self._inner_list[i2], self._inner_list[i1]
        self.callback([i1, i2], [i1, i2])

    ###############
    #  overrides  #
    ###############
    def insert(self, index: int, object) -> None:
        self._inner_list.insert(index, object)
        self.callback([], list(range(index, self._inner_list.__len__())))

    def __getitem__(self, i: int):
        item = self._inner_list.__getitem__(i)

        if type(i) == slice:
            pass
        else:
            self.callback([i], [])

        return item

    def __setitem__(self, i: int, o: _T) -> None:
        self._inner_list.__setitem__(i, o)

        if type(i) == slice:
            self.callback([], list(range(i.start, i.stop, i.step if i.step is not None else 1)))
        else:
            self.callback([], [i])

    def __delitem__(self, i: int) -> None:
        self._inner_list.__delitem__(i)
        self.callback([], list(range(i, self._inner_list.__len__())))

    def __len__(self) -> int:
        return self._inner_list.__len__()

    def __str__(self):
        return f'CallbackList{self._inner_list.__str__()}'