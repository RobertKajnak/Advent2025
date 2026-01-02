import numpy as np


class JB:
    def __init__(self, coords: tuple) -> None:
        self.coords = coords
        self.connections = set()

    def dist(self, jb: "JB") -> float:
        return np.linalg.norm(jb.coords - self.coords)

    def __repr__(self) -> str:
        return f"JB w/ Coords: {self.coords}, connected to {len(self.connections)}"

    def __eq__(self, __value: object) -> bool:
        return np.all(self.coords == __value.coords)

    def __hash__(self) -> int:
        return int(sum([10 ** (idx * 6) * c for idx, c in enumerate(self.coords)]))


boxes: list[JB] = []

with open("lvl8-0.txt", "r") as f:
    for line in f.readlines():
        boxes.append(
            JB(np.array(tuple(int(coord) for coord in line.strip().split(","))))
        )


def find_closest(target: JB, boxes: list[JB]) -> tuple[JB, float]:
    min_dist = 999999999
    min_do = None
    for jb in boxes:
        if jb != target and jb not in target.connections:
            if (new_dist := jb.dist(target)) < min_dist:
                min_dist = new_dist
                min_do = jb

    return min_do, min_dist


# for box in boxes:
#     print(box)

# jb = boxes[0]
# closest, _ = find_closest(jb, boxes)
# jb.connections.add(closest)
# closest.connections.add(jb)

for i in range(10):
    closes_pair = None
    closes_pair_dist = 9999999999
    for idx, jb in enumerate(boxes[:-1]):
        closest_box, closest_dist = find_closest(jb, boxes[idx:])

        if closest_dist < closes_pair_dist:
            closes_pair_dist = closest_dist
            closes_pair = (closest_box, jb)

    closes_pair[1].connections.add(closes_pair[0])
    closes_pair[0].connections.add(closes_pair[1])

for jb in boxes:
    print(jb)
# jb.connections.add(closest)
# closest.connections.add(jb)
