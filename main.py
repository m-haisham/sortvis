import sys
import time

import pygame

from core import colors, Switch, Vector2D
from visualizer import BarManager
from visualizer.sorting import CocktailSort
from widgets import Text, WidgetManager, Button

pygame.init()
infoObject = pygame.display.Info()
size = width, height = infoObject.current_w, infoObject.current_h - 30
screen = pygame.display.set_mode(size)

should_sort = Switch(False)
bars = BarManager(screen, int(width / 2))
bars.shuffle()

sort = CocktailSort(bars.sizes).sort_generator()
# sort = InsertionSort(bars.sizes).sort_generator()

flip_button = Button(Text('RUNNING' if should_sort.get() else 'STOPPED'), size=Vector2D(70, 25), onclick=lambda _: should_sort.flip())
flip_button.position = Vector2D(Vector2D.center(screen.get_rect(), screen.get_rect().size).x - (flip_button.size.x / 2), 0)


def fbflip(val):
    flip_button.text.text = 'RUNNING' if val else 'STOPPED'


should_sort.onflip = fbflip
manager = WidgetManager([flip_button])

framerate = 0
t0 = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                should_sort.flip()

    screen.fill(colors.WHITE)

    # manager.update()
    # manager.draw(screen)

    # bars
    bars.draw()

    if should_sort.get():
        try:
            next(sort)
        except StopIteration:
            should_sort.set(False)

    bars.generate_bars(bars.sizes)

    t1 = time.time()
    framerate = 1 / (t1 - t0)
    t0 = t1

    manager.update()
    manager.draw(screen)
    Text(f'{len(bars.sizes)} bars, {framerate:.2f} fps').draw(screen)

    pygame.display.flip()
