from .algorithm import Algorithm


class QuickSort(Algorithm):
    def __init__(self, array, low, high):
        super(QuickSort, self).__init__(array)

        self.initial_low = low
        self.initial_high = high

    def sort(self):
        self.quicksort(self.initial_low, self.initial_high)

    def partition(self, low, high):

        pivot = self.array[high]

        i = (low - 1)

        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.array.swap(i, j)

        self.array.swap(i+1, high)
        return i + 1

    def quicksort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)

            self.quicksort(low, pivot - 1)
            self.quicksort(pivot + 1, high)
