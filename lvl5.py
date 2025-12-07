import numpy as np                  


fresh = []
S = 0

# lvl 1
with open("lvl5-1.txt", "r") as f:
    lit = f.readlines().__iter__()
    for line in lit:

        if line == "\n":
            break
        fresh.append([int(ing) for ing in line.strip().split("-")])
    
    for line in lit:
        ingredient = int(line.strip())
        for fresh_range in fresh:
            if ingredient>=fresh_range[0] and ingredient<=fresh_range[1]:
                
                S += 1
                break

print(S)

# lvl 2
def inside(what, froom, too):
    return what>=froom and what<=too

def append_except(too:list, froom:list, idx1, idx2):
    for idx,f in enumerate(froom):
        if idx != idx1 and idx != idx2:
            too.append(f)

def add_one(fresh):
    compacted = []
    for idx, fr in enumerate(fresh):
        for idc, candidate in enumerate(fresh):
            if idx!=idc:
                if inside(fr[0], *candidate):
                    
                    if inside(fr[1], *candidate):
                        compacted.append(candidate)
                        append_except(compacted, fresh, idx, idc)
                        print(f"{fr} is contained inside {candidate}")
                        return compacted

                    compacted.append(new_range := [candidate[0], fr[1]])
                    append_except(compacted, fresh, idx, idc)
                    print(f"First {new_range} <- {fr} + {candidate}")
                    return compacted

                if inside(fr[1], *candidate):
                    compacted.append(new_range := [fr[0], candidate[1]])
                    append_except(compacted, fresh, idx, idc)
                    print(f"Last {new_range} <- {fr} + {candidate}")
                    return compacted

print(f"Original: {fresh}")
while True:
    new_fresh = add_one(fresh)

    if new_fresh is None:
        break
    fresh = new_fresh

print(f"Compacted: {fresh}")

S = 0
for fr in fresh:
    S += fr[1]-fr[0]+1

print(S)