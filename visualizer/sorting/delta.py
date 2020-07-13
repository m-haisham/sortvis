from typing import List, Set, Tuple


class ListDelta:
    accesses: List[int]
    writes: List[int]
    snapshot: List[float]

    highlight = Set[int]
    changes = List[Tuple[int, float]]

    def __init__(self, accesses, writes, snapshot):
        self.accesses = accesses
        self.writes = writes
        self.snapshot = snapshot

        # pre calculated data
        self.changes = [(i, snapshot[i]) for i in set(self.accesses + self.writes)]
