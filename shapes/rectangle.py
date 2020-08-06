import pygame

from core import Vector2D, Color
from .shape import Shape


class Rectangle(Shape):
    def __init__(self, position: Vector2D, size: Vector2D, color: Color):
        self.position = position
        self.size = size
        self._color = color
        self.size_color = color[:]

        self.surface = pygame.Surface(self.size)
        self.surface.fill(color)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self.surface.fill(value)

    @property
    def blit_sequence(self):
        return self.surface, self.position

    def draw(self, surface):
        surface.blit(self.surface, self.position)