from typing import List, Set, Tuple


class ListDelta:
    accesses: List[int]
    writes: List[int]
    snapshot: List[float]

    highlight = Set[int]
    access_changes = List[Tuple[int, float]]
    write_changes = List[Tuple[int, float]]

    def __init__(self, accesses, writes, snapshot):
        self.accesses = accesses
        self.writes = writes
        self.snapshot = snapshot

        # pre calculated data
        self.access_changes = [(i, snapshot[i]) for i in self.accesses]
        self.write_changes = [(i, snapshot[i]) for i in self.writes]
