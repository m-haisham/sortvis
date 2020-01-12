import pygame

from core import Vector2D, input


class WidgetManager:
    def __init__(self, widgets: list = None):
        self.widgets = widgets
        if self.widgets is None:
            self.widgets = []

    def draw(self, surface):
        for widget in self.widgets:
            widget.draw(surface)

    def update(self):

        mouse_input: input.Mouse = input.Mouse.instance
        mouse_pos = Vector2D.from_tuple(pygame.mouse.get_pos())

        for widget in self.widgets:

            widget.update(mouse_input)

            mouse_is_over = widget.is_mouse_over(mouse_pos)

            if mouse_is_over:
                if mouse_input.left.pressed:
                    clicked = getattr(widget, 'clicked', None)
                    if callable(clicked):
                        widget.clicked()

            if not widget.hover and mouse_is_over:
                widget.enter()

            if widget.hover and not mouse_is_over:
                widget.exit()
