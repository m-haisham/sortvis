from .algorithm import Algorithm


class QuickSort(Algorithm):
    pivot: int

    def __init__(self, array, low, high):
        super(QuickSort, self).__init__(array)

        self.initial_high = high
        self.initial_low = low

    def iterative_sort(self):
        for a in self.quicksort(self.initial_low, self.initial_high):
            yield a

    def partition(self, low, high):

        pivot = self.array[high]

        i = (low - 1)

        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

                yield self.array

        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        yield self.array

        self.pivot = i + 1

    def quicksort(self, low, high):
        if low < high:

            for a in self.partition(low, high):
                yield a

            for a in self.quicksort(low, self.pivot - 1):
                yield a

            for a in self.quicksort(self.pivot + 1, high):
                yield a
