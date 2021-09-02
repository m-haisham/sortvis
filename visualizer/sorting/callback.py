from collections import MutableSequence
from typing import List, Callable, TypeVar

_T = TypeVar('_T')


class CallbackList(MutableSequence):
    """
    callback on each change to sequence with indexes that changed
    """

    # callback(accessed_indexes, written_indexes)
    callback: Callable[[List[int], List[int], List], None]

    def __init__(self, callback, li: List = None):

        # initialize callback function
        self.callback = callback

        # initialize inner list
        if li is None:
            self._inner_list = []
        else:
            self._inner_list = li

    def swap(self, i1: int, i2: int):
        """
        swap value of index one with other

        it is recommended to use this for swaps
        """
        self._inner_list[i1], self._inner_list[i2] = self._inner_list[i2], self._inner_list[i1]

        # bubble up swap info
        self.callback([i1, i2], [i1, i2], self.copy_discrete())

    def insert(self, index: int, obj) -> None:
        self._inner_list.insert(index, obj)

        # bubble up what has changed
        self.callback([], list(range(index, self._inner_list.__len__())), self.copy_discrete())

    def __getitem__(self, i):
        item = self._inner_list.__getitem__(i)

        # bubble up what was accessed
        if type(i) == slice:
            start = i.start if i.start else 0
            stop = i.stop if i.stop else len(self)

            self.callback(list(range(start, stop)), [], self.copy_discrete())

            def _callback(r, w, c):
                array_copy = self.copy_discrete()
                array_copy[start:stop] = c

                return self.callback(
                    [start + i for i in r],
                    [start + i for i in w],
                    array_copy,
                )

            return CallbackList(_callback, item)
        else:
            self.callback([i], [], self.copy_discrete())

        return item

    def __setitem__(self, i, o: _T) -> None:
        self._inner_list.__setitem__(i, o)

        # bubble up what has changed
        if type(i) == slice:
            self.callback([], list(range(i.start, i.stop, i.step if i.step else 1)), self.copy_discrete())
        else:
            self.callback([], [i], self.copy_discrete())

    def __delitem__(self, i: int) -> None:
        self._inner_list.__delitem__(i)

        # bubble up what has changed
        self.callback([], list(range(i, self._inner_list.__len__())), self.copy_discrete())

    def __len__(self) -> int:
        return self._inner_list.__len__()

    def __str__(self):
        return f'CallbackList{self._inner_list.__str__()}'

    def copy_discrete(self):
        return self._inner_list.copy()
