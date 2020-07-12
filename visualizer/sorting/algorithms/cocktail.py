from .algorithm import Algorithm


class CocktailSort(Algorithm):
    def __init__(self, array):
        super(CocktailSort, self).__init__(array)

    def sort(self):
        n = len(self.array)
        swapped = True
        start = 0
        end = n - 1
        while swapped:

            # reset the swapped flag on entering the loop,
            # because it might be true from a previous
            # iteration.
            swapped = False

            # loop from left to right same as the bubble
            # sort
            for i in range(start, end):
                if self.array[i] > self.array[i + 1]:
                    self.array.swap(i, i + 1)
                    swapped = True

            # if nothing moved, then array is sorted.
            if not swapped:
                break

            # otherwise, reset the swapped flag so that it
            # can be used in the next stage
            swapped = False

            # move the end point back by one, because
            # item at the end is in its rightful spot
            end = end - 1

            # from right to left, doing the same
            # comparison as in the previous stage
            for i in range(end - 1, start - 1, -1):
                if self.array[i] > self.array[i + 1]:
                    self.array.swap(i, i + 1)
                    swapped = True

            # increase the starting point, because
            # the last stage would have moved the next
            # smallest number to its rightful spot.
            start = start + 1
