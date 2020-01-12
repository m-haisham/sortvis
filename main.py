import sys
import time

import pygame

from core import colors, Switch, Vector2D, Color
from visualizer import BarManager
from visualizer.sorting import InsertionSort, CocktailSort, CycleSort
from widgets import Text, WidgetManager, Button, Hover
from widgets.button import WHITE_TEXT_TRANSPARENT_BACKGROUND, BLACK_TEXT_WHITE_BACKGROUND

pygame.init()
infoObject = pygame.display.Info()
size = width, height = infoObject.current_w, infoObject.current_h - 30
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Sorting visualizer')

should_sort = Switch(False)
bars = BarManager(screen, int(width / 4))
bars.shuffle()

# change this as necessary to change sorting algorithm
# sortg = CocktailSort(bars.sizes).sort_generator()
# sortg = InsertionSort(bars.sizes).sort_generator()
sortg = CycleSort(bars.sizes).sort_generator()

flip_button = Button(Text('', color=colors.WHITE), size=Vector2D(70, 25), color=Color(0, 0, 0, 0), onclick=lambda _: should_sort.flip())
flip_button.position = Vector2D(Vector2D.center(screen.get_rect(), screen.get_rect().size).x - (flip_button.size.x / 2), 0)
flip_button.onhover = Hover(BLACK_TEXT_WHITE_BACKGROUND, WHITE_TEXT_TRANSPARENT_BACKGROUND)

def fbflip(val):
    flip_button.text.text = 'RUNNING' if val else 'STOPPED'


fbflip(should_sort.get())
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

    screen.fill(colors.BLACK)

    # bars
    bars.draw()

    if should_sort.get():
        try:
            next(sortg)
        except StopIteration:
            should_sort.set(False)

    bars.generate_bars(bars.sizes)

    t1 = time.time()
    framerate = 1 / (t1 - t0)
    t0 = t1

    manager.update()
    manager.draw(screen)
    Text(f'{sortg.__qualname__.split(".")[0]}, {len(bars.sizes)} bars, {framerate:.2f} fps', color=colors.WHITE).draw(screen)

    pygame.display.flip()
