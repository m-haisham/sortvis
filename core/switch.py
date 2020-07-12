from typing import Callable, Any, Union


class Switch:
    on_flip: Callable[[bool], None]

    def __init__(self, default=False, on_flip: Callable[[bool], None] = None):
        self._value = default

        if on_flip is None:
            on_flip = lambda _: None
        self.on_flip = on_flip

    def flip(self):
        self._value = not self._value
        self.on_flip(self.get())

    def set(self, value: bool):
        self._value = value
        self.on_flip(self.get())

    def get(self):
        return self._value
