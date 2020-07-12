import random

from typing import Dict

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

        self.bars: Dict[str, Rectangle] = {}
        self.generate_bars(self.sizes)

        # color changed tracker
        self.previous_changed = []

    def shuffle(self):
        random.shuffle(self.sizes)

    def generate_bars(self, sizes):
        bar_width = self.surface.get_rect().size[0] / self.size

        for i, y in enumerate(sizes):

            try:
                bar = self.bars[y]
                bar.position = Vector2D.custom(self.surface, i * bar_width, y - 1, inverty=True)
                continue
            except KeyError:
                bar = Rectangle(
                    Vector2D.custom(self.surface, i * bar_width, y - 1, inverty=True),
                    Vector2D(bar_width, y),
                    Color.lerp(y / self.max, colors.RED, colors.GREEN, colors.BLUE)
                )

                self.bars[y] = bar

    def update_bars(self, sizes):
        bar_width = self.surface.get_rect().size[0] / self.size

        for i, y in sizes:
            bar = self.bars[y]
            bar.position = Vector2D.custom(self.surface, i * bar_width, y - 1, inverty=True)

    def draw(self, updated=None):
        """
        draw all the [bars] in class
        if bar size is in changed color it white

        :param updated: bars that have changed
        :return: None
        """
        # reset previous color changed
        while True:
            try:
                bar = self.bars[self.previous_changed.pop()]
                bar.color = bar.size_color[:]
            except IndexError:
                break

        # change color of updated bars
        if updated is not None:
            for _, size in updated:
                self.bars[size].color = colors.WHITE
                self.previous_changed.append(size)

        # draw
        for bar in self.bars.values():
            bar.draw(self.surface)
