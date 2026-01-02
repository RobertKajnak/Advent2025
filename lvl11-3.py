import numpy as np                  
from dataclasses import dataclass
from collections import deque
S= 0
rows = []

@dataclass
class Edge:
    to:str
    used:bool

    def __repr__(self):
        return f" -> {self.to} "

    

class Graph:
    def __init__(self):
        self.edges :dict[str, list[Edge]]= {}
        self.nodes:dict[str, np.ndarray ] = {}

    def add_edge(self, frm:str, to:str):
        if frm not in self.edges:
            self.edges[frm] = []
        self.edges[frm].append(Edge(to, False))

    def dfs(self, start_node:str, end_node:str, visited_nodes:list[str]):
        # if len(succesful_paths)==10000000:
        #     return
        reached_end = np.array((0,0,0, 0))
        for edge in self.edges[start_node]:
            # print(edge)
            if edge.to in self.nodes:
                
                print(f"1: {visited_nodes}")
                reached_end += self.nodes[edge.to]
            else:
                if not edge.used:
                    if edge.to == end_node:
                        # if "fft" in path_taken and "dac" in path_taken:
                        # new_path = path_taken + [start_node, end_node]
                        # succesful_paths.append(new_path)
                        print(f"2: {visited_nodes}")
                        reached_end += np.array((1,0,0,0))
                        #     print(f"Added good path @ {len(succesful_paths)}")
                        # if len(succesful_paths)%100000 == 0:
                        # print(len(succesful_paths))
                        
                    else:
                        edge.used = True
                        # path_taken.append(start_node)
                        reached_end += self.dfs(edge.to,end_node, visited_nodes + [edge.to])
                        # path_taken.pop()
                        edge.used = False
        # if start_node not in self.nodes:

        sub_end = reached_end
        if "dac" == start_node:
            sub_end[3] += sub_end[2]
            sub_end[2] = 0
            sub_end[1] += sub_end[0]
            sub_end[0] = 0

        if  "fft" == start_node:
            sub_end[3] += sub_end[1]
            sub_end[1] = 0
            sub_end[2] += sub_end[0]
            sub_end[0] = 0

        self.nodes[start_node] = reached_end
        # else:
        #     self.nodes[start_node] += reached_end
        return reached_end
        

    def total_capacity(self, start_node:str, end_node:str):
        self.dfs(start_node, end_node, [start_node])            
        return self.nodes[start_node]

    def __repr__(self):
        return "\n".join((frm+str(edge) for frm, edge in self.edges.items()))

g = Graph()
with open("lvl11-1.txt", "r") as f:

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
# g.dfs("you", "out")
print("===")
totcap = g.total_capacity("svr", "out")
print("----")
# print(g)
print(f"finished in {time.time()- start}")
print(totcap) # lvl 1
# print(len(successful_paths)) # lvl 1

# lvl_2_paths = [sfp for sfp in successful_paths if "fft" in sfp and "dac" in sfp]
    
# print(lvl_2_paths) # lvl 2
# print(len(lvl_2_paths)) # lvl 2

# Nope: 307041755439226896