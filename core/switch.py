class Switch:
    def __init__(self, default=False):
        self._value = default

    def flip(self):
        self._value = not self._value

    def set(self, value: bool):
        self._value = value

    def get(self):
        return self._value