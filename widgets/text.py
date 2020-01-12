import pygame

from core import Color, colors, Vector2D
from core.fonts import Roboto, Font
from .widget import Widget


class Text(Widget):
    surface: pygame.SurfaceType

    def __init__(self, text, size=14, italic=False, color: Color = colors.BLACK, font: Font = Roboto.MEDIUM):
        super(Text, self).__init__()

        self.text = text

        self.surface = font.get(size, italic).render(text, True, color)
        self.position = Vector2D(0, 0)

    def center(self, position):
        size = self.surface.get_rect().size

        self.position = Vector2D(
            position.x - (size[0] / 2),
            position.y - (size[1] / 2)
        )

    def draw(self, surface):
        surface.blit(self.surface, self.position)