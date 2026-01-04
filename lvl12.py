import numpy as np
from time import time
import re


def hash(array:np.ndarray):
    
    S = 0
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            S += 2<<(i*array.shape[0]+j)*int(array[i,j])
    return S



class Tile:
    def __init__(self, value:np.ndarray):
        self.value = value

    def variants(self) -> list["Tile"]:
        variants = {}
        # variants[self.__hash__()] = self.value
        rotated = self.value
        for _ in range(4):
            variants[hash(rotated)] = Tile(rotated)

            flipped = np.fliplr(rotated)
            variants[hash(flipped)] = Tile(flipped)

            flipped = np.flipud(rotated)
            variants[hash(flipped)] = Tile(flipped)

            flipped = np.fliplr(flipped)
            variants[hash(flipped)] = Tile(flipped)
            
            rotated = np.rot90(self.value)
        
        return variants.values()
        
    def fits(self, target:np.ndarray, x, y):
        if isinstance(target, Tile):
            target = target.value

        for i in range(target.shape[0]):
            if x+i>=self.value.shape[0]:
                return False
            for j in range(target.shape[1]):
                if y+j>=self.value.shape[1]:
                    return False
                if target[i,j] and self.value[x+i, y+j]:
                    return False
        return True
    
    def add(self, target:np.ndarray, x, y):
        if isinstance(target, Tile):
            target = target.value
    
        for i in range(target.shape[0]):
            for j in range(target.shape[1]):
                self.value[x+i, y+j] |= target[i,j]

    def subtract(self, target:np.ndarray, x, y):
        if isinstance(target, Tile):
            target = target.value

        for i in range(target.shape[0]):
            for j in range(target.shape[1]):
                if target[i,j]:
                    self.value[x+i, y+j] = False


    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, value):
        return self.__hash__ == value.__hash__()
    
    def __repr__(self):
        return "\n" + "\n".join(["".join(["■" if self.value[i,j] else "□" for j in range(self.value.shape[1])]) for i in range(self.value.shape[0])]) +"\n"

with open("lvl12-0.txt", "r") as f:
    contents = f.read()
shapes_raw = list(re.finditer(r"\d\:\n((?:[\.#]{3}\n){3})", contents))
shapes = tuple(Tile(np.array(tuple(tuple(c=="#"  for c in line) for line  in shape.groups()[0].strip().split("\n")))) for shape in shapes_raw)


def _find_fit(space:Tile,tile:Tile):
    variants = list(tile.variants())
    for variant in variants:
        for i in range(w-2):
            for j in range(h-2):
                if space.fits(variant,i,j):
                    space.add(variant,i,j)
                    if tile is variants[-1]:
                        return variant, i,j
                    break
    return None

def tile_bruteforce(w:int,h:int,tiles:list[Tile]):
    space = Tile(np.array(np.zeros(shape= (w,h))==1))

    for tile in tiles:
        successful_fit = _find_fit(space, tile)
        
    

for line in contents[ shapes_raw[-1].span()[1]:].split("\n"):
    if len(line)<=1:
        continue
    w, h, quantities = re.findall(r"(\d+)x(\d+)\: (.*)",line)[0]
    w = int(w)
    h = int(h)
    quantities = [int(i) for i in quantities.strip().split()]
    tile_set = []
    for sh_idx, q  in enumerate(quantities):
        for _ in range(q):
            tile_set.append(shapes[sh_idx])

    
    print(w,h,quantities) 
    print(tile_bruteforce(w,h,tile_set))
    break