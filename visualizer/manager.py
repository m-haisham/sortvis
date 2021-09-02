import random

from typing import Dict

from core import Vector2D, colors, Color
from shapes import Rectangle


class BarManager:
    def __init__(
            self,
            surface,
            length=None,
            shuffle=False,
            color=None,
            highlight_accessed=colors.GREEN,
            highlight_written=colors.RED,
    ):
        """
        :param surface: pygame surface to draw the bars
        :param length: amount of bars
        :param shuffle: whether to shuffle the bars on init
        :param color: color of bars
        :param highlight: color of bars to when it has changed
        """
        self.surface = surface
        self.color = color
        self.highlight_accessed = highlight_accessed
        self.highlight_written = highlight_written

        if length is None:
            # one bar for each pixel
            length = surface.get_rect().size[0]
        self.size = length

        accuracy = 1000
        self.sizes = [i / accuracy for i in range(
            1,
            self.surface.get_rect().size[1] * accuracy + 1,
            int((self.surface.get_rect().size[1] * accuracy / length)))
        ]
        self.max = self.surface.get_rect().size[1]

        # graphic rectangles
        self.bars: Dict[str, Rectangle] = {}

        if shuffle:
            self.shuffle()

        self.generate_bars(self.sizes)

        # color changed tracker
        self.previous_changed = []

    def shuffle(self):
        """
        inline shuffle sizes
        """
        random.shuffle(self.sizes)

    def generate_bars(self, sizes):
        """
        creates the bars if they aren't already, else updates them

        :param sizes: sizes of bars
        :return:
        """
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

                    color=Color.lerp(y / self.max, colors.RED, colors.GREEN, colors.BLUE)
                    if self.color is None else self.color
                )

                self.bars[y] = bar

    def update_bars(self, accesses, writes):
        """Update bar position using the new size"""
        bar_width = self.surface.get_rect().size[0] / self.size

        # reset previous color changed
        while True:
            try:
                bar = self.bars[self.previous_changed.pop()]
                bar.color = bar.size_color[:]
            except IndexError:
                break

        self._update_change(bar_width, accesses, self.highlight_accessed)
        self._update_change(bar_width, writes, self.highlight_written)

    def _update_change(self, bar_width, sizes, color):
        for i, y in sizes:
            bar = self.bars[y]
            bar.position = Vector2D.custom(self.surface, i * bar_width, y - 1, inverty=True)

            # highlight the bar
            bar.color = color
            self.previous_changed.append(y)

    def draw(self):
        """
        draw all the [bars] in class
        if bar size is in changed color it white

        :return: None
        """
        self.surface.blits([bar.blit_sequence for bar in self.bars.values()])
