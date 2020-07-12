## Sortvis

A simple sorting algorithm visualizer written in pygame

#### Instructions

each algorithm should inherit `visualizer.sorting.Algorithm`

```python
class Algorithm:
    def __init__(self, array: list):
        self.array = array

    def sort_generator(self):
        """
        yields the new array after each sort iteration
        """
        pass
       
    # optional
    def sort(self):
        """
        sort the whole array
        """
        pass
```

change `sorta` variable to another sort as shown in `main.py`

```python
sorta = CocktailSort(bars.sizes)
# sorta = InsertionSort(bars.sizes)
```

you can start or stop sort by using button on top-center or by pressing `Space`
