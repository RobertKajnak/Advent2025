import numpy as np                  
from dataclasses import dataclass
from collections import deque
S= 0
rows = []

@dataclass
class Edge:
    to:str
    used:bool
    flow:int = None

    def __repr__(self):
        return f" -> {self.to}"
    

class Graph:
    def __init__(self):
        self.nodes :dict[str, list[Edge]]= {}

    def add_edge(self, frm:str, to:str):
        if frm not in self.nodes:
            self.nodes[frm] = []
        self.nodes[frm].append(Edge(to, False))

    def dfs(self, start_node:str, end_node:str, succesful_paths:list[list[str]]):
        # if len(succesful_paths)==10000000:
        #     return
        for edge in self.nodes[start_node]:
            reached_end = 0
            if not edge.used:
                if edge.to == end_node:
                    # if "fft" in path_taken and "dac" in path_taken:
                    new_path = path_taken + [start_node, end_node]
                    succesful_paths.append(new_path)
                    reached_end += 1
                    #     print(f"Added good path @ {len(succesful_paths)}")
                    # if len(succesful_paths)%100000 == 0:
                    # print(len(succesful_paths))
                    return
                else:
                    edge.used = True
                    # path_taken.append(start_node)
                    self.dfs(edge.to,end_node, path_taken, succesful_paths)
                    # path_taken.pop()
                    edge.used = False
            

    def __repr__(self):
        return "\n".join((frm+str(edge) for frm, edge in self.nodes.items()))

g = Graph()
with open("lvl11-0.txt", "r") as f:

    for line in f.readlines():
        nodes = line.strip().split()
        frm = nodes[0][:-1]
        to = nodes[1:]

        for t in to:
            g.add_edge(frm, t)

import time
print(g)
successful_paths = deque()
# g.dfs("you", "out", [], successful_paths) # part 1
start = time.time()
g.dfs("you", "out", [], successful_paths)
print(f"finished in {time.time()- start}")
# print(successful_paths) # lvl 1
print(len(successful_paths)) # lvl 1

# lvl_2_paths = [sfp for sfp in successful_paths if "fft" in sfp and "dac" in sfp]
    
# print(lvl_2_paths) # lvl 2
# print(len(lvl_2_paths)) # lvl 2