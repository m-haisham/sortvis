from .algorithm import Algorithm


class CycleSort(Algorithm):
    def __init__(self, array):
        super(CycleSort, self).__init__(array)

    def sort(self):
        # Loop through the array to find cycles to rotate.
        for cycleStart in range(0, len(self.array) - 1):
            item = self.array[cycleStart]

            # Find where to put the item.
            pos = cycleStart
            for i in range(cycleStart + 1, len(self.array)):
                if self.array[i] < item:
                    pos += 1

            # If the item is already there, this is not a cycle.
            if pos == cycleStart:
                continue

            # Otherwise, put the item there or right after any duplicates.
            while item == self.array[pos]:
                pos += 1
            self.array[pos], item = item, self.array[pos]

            # Rotate the rest of the cycle.
            while pos != cycleStart:

                # Find where to put the item.
                pos = cycleStart
                for i in range(cycleStart + 1, len(self.array)):
                    if self.array[i] < item:
                        pos += 1

                # Put the item there or right after any duplicates.
                while item == self.array[pos]:
                    pos += 1
                self.array[pos], item = item, self.array[pos]
