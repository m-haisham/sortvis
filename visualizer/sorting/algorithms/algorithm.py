from typing import Union

from ..callback import CallbackList


class Algorithm:
    array: CallbackList

    def __init__(self, array: Union[CallbackList, list]):

        # initialize array
        if type(array) == list:
            self.array = CallbackList(lambda _: None, array)
        else:
            self.array = array

    def sort(self):
        """
        sort the whole array
        """
        raise NotImplementedError
