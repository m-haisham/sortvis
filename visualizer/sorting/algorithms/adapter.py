from typing import Union, Callable

from .algorithm import Algorithm
from ..callback import CallbackList


class SortAdapter(Algorithm):
    def __init__(self, array: Union[CallbackList, list], func: Callable[[Union[CallbackList, list]], None]):
        super(SortAdapter, self).__init__(array)

        self.func = func

    def sort(self):
        self.func(self.array)
