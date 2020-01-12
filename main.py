import sys
import time

import pygame

from core import colors, Switch
from visualizer import BarManager
from visualizer.sorting import CocktailSort
from widgets import Text

pygame.init()
size = width, height = 1024, 600
screen = pygame.display.set_mode(size)

should_sort = Switch(False)
bars = BarManager(screen, int(width / 2))
bars.shuffle()

sort = CocktailSort(bars.sizes).sort_generator()
# sort = InsertionSort(bars.sizes).sort_generator()

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

    Text(f'{len(bars.sizes)} bars, {framerate:.2f} fps').draw(screen)

    pygame.display.flip()
