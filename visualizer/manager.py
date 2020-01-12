import random

from core import Vector2D, colors, Color
from shapes import Rectangle


class BarManager:
    def __init__(self, surface, size=None):
        self.surface = surface

        if size is None:
            size = surface.get_rect().size[0]
        self.size = size

        accuracy = 1000
        self.sizes = [i / accuracy for i in range(
            1,
            self.surface.get_rect().size[1] * accuracy + 1,
            int((self.surface.get_rect().size[1] * accuracy / size)))
        ]
        self.max = self.surface.get_rect().size[1]

        self.generate_bars(self.sizes)

    def shuffle(self):
        random.shuffle(self.sizes)

    def generate_bars(self, sizes):
        self.bars = []

        bar_width = self.surface.get_rect().size[0] / self.size
        for i, y in zip(range(self.size), sizes):
            bar = Rectangle(
                Vector2D.custom(self.surface, i * bar_width, y - 1, inverty=True),
                Vector2D(bar_width, y),
                Color.lerp(y / self.max, colors.RED, colors.GREEN, colors.BLUE, colors.PURPLE)
            )

            self.bars.append(bar)

    def draw(self):
        for bar in self.bars:
            bar.draw(self.surface)
