import os
import sys
import time

import pygame
from pygame.locals import DOUBLEBUF

from core import colors, Switch, Vector2D, Color
from visualizer import BarManager
from visualizer.sorting import AlgorithmController
from visualizer.sorting.algorithms import InsertionSort, CocktailSort, CycleSort, QuickSort
from widgets import Text, WidgetManager, Button, Hover
from widgets.button import WHITE_TEXT_TRANSPARENT_BACKGROUND, BLACK_TEXT_WHITE_BACKGROUND

ytrans = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = f'0,{ytrans}'

pygame.init()
infoObject = pygame.display.Info()
size = width, height = infoObject.current_w, infoObject.current_h - ytrans
screen = pygame.display.set_mode(size, DOUBLEBUF)

pygame.display.set_caption('Sorting visualizer')
pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN])

should_sort = Switch(False)
bars = BarManager(screen, int(width / 4))
# bars = BarManager(screen, 100)
bars.shuffle()
bars.generate_bars(bars.sizes)
bars_range = range(len(bars.sizes))

# change this as necessary to change sorting algorithm
# sorta = CocktailSort(bars.sizes[:])
# sorta = InsertionSort(bars.sizes[:])
# sorta = CycleSort(bars.sizes[:])
sorta = QuickSort(bars.sizes[:], 0, len(bars.sizes) - 1)

ac = AlgorithmController(sorta)
ac.start()

# button to control algorithm flow
flip_button = Button(
    Text('', color=colors.WHITE),
    size=Vector2D(70, 25),
    color=Color(0, 0, 0, 0),
    onclick=lambda _: should_sort.flip()
)
flip_button.position = Vector2D(
    Vector2D.center(screen.get_rect(), screen.get_rect().size).x - (flip_button.size.x / 2),
    0
)
flip_button.onhover = Hover(BLACK_TEXT_WHITE_BACKGROUND, WHITE_TEXT_TRANSPARENT_BACKGROUND)


def fbflip(val):
    flip_button.text.text = 'RUNNING' if val else 'STOPPED'


fbflip(should_sort.get())
should_sort.on_flip = fbflip
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

        manager.event(event)

    screen.fill(colors.BLACK)

    # update and draw bars
    changed = []
    if should_sort.get():
        try:
            indexes, bars.sizes = next(ac.iterator)
            changed = [(i, bars.sizes[i]) for i in indexes]
        except StopIteration:
            should_sort.set(False)

    bars.update_bars(changed)
    bars.draw(changed)

    # calculate framerate
    t1 = time.time()
    framerate = 1 / (t1 - t0)
    t0 = t1

    manager.update()
    manager.draw(screen)

    # information display
    Text(
        f'{sorta.__class__.__name__.split(".")[0]}, {len(bars.sizes)} bars, '
        f'Accesses: {ac.accesses}, Writes: {ac.writes}, '
        f'{framerate:.2f} fps',
        color=colors.WHITE
    ).draw(screen)

    pygame.display.flip()
