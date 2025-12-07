import numpy as np                  
S= 0
rows = []
with open("lvl7-0.txt", "r") as f:

    for line in f.readlines():
        rows.append(line.strip())

m = np.zeros((len(rows), len(rows[0])))

start = (0,0)
for ri, row in enumerate(rows):
    for ci, c in enumerate(row):
        if c == "^":
            m[ri, ci] = 1
        elif c=="S":
            start = (ri, ci)


def propagate_down(x,y, maxx, S):
    while x<maxx-1:

        x +=1
        # print(f"visiting {(x,y )} == {m[x,y]}")
        # print(m)
        # print()
        m[x-1, y] = 2
        if m[x,y] == 2:
            # print("Already visisted")
            return S
        if m[x, y]:
            # print("true")
            S += propagate_down(x, y+1, maxx, 0)
            y = y-1
            S +=1
    # print("==============finished")
    return S

# print(start)
# print(m)
try:
    S = propagate_down(*start, m.shape[0], 0)
except IndexError:
    print("Ended in error")
# v = np.char.chararray(shape=m.shape)
# for i in range(m.shape[0]):
#     for j in range(m.shape[1]):
#         v[i,j] = "-" if m[i, j] == 0 else ("^" if m[i,j] == 1 else "|")
print("\n")
print(m)
print(S)
