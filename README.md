# Sortvis

A simple sorting algorithm visualizer written in pygame

**Displays number of list accesses and writes**

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

### Add a new algorithm

Each algorithm should inherit `visualizer.sorting.Algorithm`
with the implementation overriding the method `sort`

#### There is only one guideline

- if you want to swap values, use the built in `CallbackList.swap(l1, l2)`.
it would work even if its not used.

Other than that **no modifications** are required

```python
class Algorithm:
    def __init__(self, array: Union[CallbackList, list]):
        if type(array) == list:
            self.array = CallbackList(lambda _: None, array)
        else:
            self.array = array

    def sort(self):
        """
        sort the whole array
        """
        raise NotImplementedError
```