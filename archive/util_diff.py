import difflib
from typing import List


class DeltaMark:
    CHANGE_POS = "?"
    CHANGE_BEFORE = "-"
    CHANGE_AFTER = "+"
    CHANGE_NO = " "


class DeltaInfo:
    def __init__(self, line):
        self.line = line
        self.delta_pos = []

    @property
    def state(self):
        return self.line[0]

    @property
    def body(self):
        return self.line[2:]

    def _append_pos(self, pos):
        p = self.delta_pos
        if p and p[-1][1] == pos:
            p[-1][1] += 1
        else:
            p.append([pos, pos+1])

    def update_delta(self, line):
        self.delta_pos = []
        for i, c in enumerate(line, 2):
            if c == self.state or c == '^':
                self._append_pos(i)


def calculate_diff(before: str, after: str) -> List[DeltaInfo]:
    before = before.splitlines()
    after = after.splitlines()

    diff = difflib.Differ()
    result = []
    for row in diff.compare(before, after):
        d = DeltaInfo(row)
        if d.state == DeltaMark.CHANGE_POS:
            if result:
                result[-1].update_delta(d.body)
        else:
            result.append(d)

    return result


