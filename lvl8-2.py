import numpy as np
import bisect


class JB:
    def __init__(self, coords: tuple) -> None:
        self.coords = coords
        self.descendants = set()
        # self.edges = set()
        self.parent = None
        # self.rank = 0
        self.size = 1

    # def add_connections(self, destinations: list["JB"]):
    #     for jb in destinations:
    #         if jb != self:
    #             bisect.insort(
    #                 self.edges, Edge(jb, self.dist(jb)), key=lambda x: x.weight
    #             )
    def is_loop(self, edge: "Edge"):
        pass

    def __repr__(self) -> str:
        return f"JB[{self.size}] w/ Coords: {self.coords} ; parent = {self.parent}"  # ; edges= {[e for e in self.edges]}"

    def __eq__(self, __value: object) -> bool:
        return np.all(self.coords == __value.coords)

    def __hash__(self) -> int:
        return int(sum([10 ** (idx * 6) * c for idx, c in enumerate(self.coords)]))


class Edge:
    def __init__(self, source: JB, dest: JB, weight: float) -> None:
        self.source = source
        self.dest = dest
        self.weight = weight

    def __repr__(self) -> str:
        return f"d({self.source.coords} <-> {self.dest.coords}) == {self.weight} "

    def __eq__(self, __value: object) -> bool:
        return (self.source == __value.source and self.dest == __value.dest) or (
            self.source == __value.dest and self.dest == __value.source
        )

    def __hash__(self) -> int:
        return 10**24 * self.source.__hash__() + self.dest.__hash__()


def dist(fr: JB, to: JB) -> float:
    return np.linalg.norm(fr.coords - to.coords)


class graph:
    def __init__(self) -> None:
        self.vertices: list[JB] = []


class Forest:
    def __init__(self, nodes: list[JB]) -> None:
        self.nodes = nodes.copy()

    def find_representative(self, node: JB) -> JB:
        while node.parent:
            node = node.parent

        return node

    def merge(self, node_1: JB, node_2: JB):
        node_1 = self.find_representative(node_1)
        node_2 = self.find_representative(node_2)
        if node_1 == node_2:
            return

        if node_1.size < node_2.size:
            node_1, node_2 = node_2, node_1

        node_2.parent = node_1
        node_1.size += node_2.size

        node_1.descendants.add(node_2)
        node_1.descendants = node_1.descendants.union(node_2.descendants)
        node_2.descendants = None

        ## Using rank:
        # if node_1.rank < node_2.rank:
        #     node_1, node_2 = node_2, node_1

        # node_2.parent = node_1

        # if node_1.rank == node_2.rank:
        #     node_1.rank += 1


g = graph()

with open("lvl8-1.txt", "r") as f:
    for line in f.readlines():
        g.vertices.append(
            JB(np.array(tuple(int(coord) for coord in line.strip().split(","))))
        )


def sorted_edges() -> list[Edge]:
    edges = []
    N = len(g.vertices)
    for i in range(N):
        for j in range(i + 1, N):
            bisect.insort(
                edges,
                Edge(x := g.vertices[i], y := g.vertices[j], dist(x, y)),
                key=lambda x: x.weight,
            )
    return edges


forest = Forest(g.vertices)
print("finished building forest")

edges = sorted_edges()
print("Finished sorting edges")

i = 0

for edge in edges:
    i += 1
    if (repr_1 := forest.find_representative(edge.source)) != (
        repr_2 := forest.find_representative(edge.dest)
    ):
        forest.merge(edge.source, edge.dest)
        # print(f"{i}. merging {edge.source.coords}, {edge.dest.coords}")
        last_merge = (edge.source.coords[0], edge.dest.coords[0])
    # if i == 10: #level 1: 10 & 1000
    #     break


#         edge.source.edges.add(edge.dest)
def level1():
    circ_sizes = []
    for node in forest.nodes:
        if node.descendants:  # is not None:
            # print(f"{node.coords} <- {[n.coords for n in node.descendants]}")
            bisect.insort(circ_sizes, len(node.descendants) + 1)

    # print(circ_sizes)
    return circ_sizes[-1] * circ_sizes[-2] * circ_sizes[-3]


# print(level1())

# level[2]
print(last_merge[0] * last_merge[1])
