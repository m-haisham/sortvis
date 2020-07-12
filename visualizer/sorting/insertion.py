from .algorithm import Algorithm


class InsertionSort(Algorithm):
    def __init__(self, array):
        super(InsertionSort, self).__init__(array)

    def sort_generator(self):
        for index, key in enumerate(self.array):
            j = index - 1

            while j > -1 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                yield self.array

                j -= 1
            self.array[j + 1] = key
            yield self.array

    def sort(self):
        for index, key in enumerate(self.array):
            j = index - 1

            while j > -1 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
