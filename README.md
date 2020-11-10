# Sortvis

A simple sorting algorithm visualizer written in pygame

**Displays number of list accesses and writes**

![Imgur](https://i.imgur.com/KCNMfsC.gif)

> Quicksort with 200 randomised starting values

## Implemented algorithms

- Cocktail sort
- Cycle sort
- Insertion sort
- Quick sort

## Change current algorithm

change `sorta` variable to another sort as shown in `main.py`

```python
sorta = CocktailSort(bars.sizes)
# sorta = InsertionSort(bars.sizes)
```

you can start or stop sort by using button on top-center or by pressing `Space`

## Want to use your own algorithm?

### Use the adapter

Any inline sort function may be passed to `SortAdapter` param `func` to create an `Algorithm`

```python

from visualizer.sorting.algorithms import SortAdapter

sorta = SortAdapter(bars.sizes, func=very_fast_sort)
```

the function should take **one parameter**, list of values to be sorted

> [Why doesnt my function work?](#known-issues)

### Write your own

Each algorithm should inherit `visualizer.sorting.Algorithm`
with the implementation overriding the method `sort`

#### Guideline

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
## Known issues

- Doesn't support creating subarrays in sort

    When subarrays are created update callbacks arent called as they should
