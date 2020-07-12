# Sortvis

A simple sorting algorithm visualizer written in pygame

## Implemented algorithms

- Cocktail sort
- Cycle sort
- Insertion sort
- Quick sort

## Instructions

### Change current algorithm

change `sorta` variable to another sort as shown in `main.py`

```python
sorta = CocktailSort(bars.sizes)
# sorta = InsertionSort(bars.sizes)
```

you can start or stop sort by using button on top-center or by pressing `Space`

### Add new algorithm

each algorithm should inherit `visualizer.sorting.Algorithm`

```python
class Algorithm:
    def __init__(self, array: list):
        self.array = array

    def iterative_sort(self):
        """
        yield changed array after change
        """
        raise NotImplementedError
       
    # optional
    def sort(self):
        """
        sort the whole array
        """
        raise NotImplementedError
```
