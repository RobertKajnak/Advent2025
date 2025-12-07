import numpy as np                  
S= 0
rows = []
with open("lvl4-0.txt", "r") as f:

    for line in f.readlines():
        rows.append(line.strip())

m = np.zeros((len(rows), len(rows[0])))

for ri, row in enumerate(rows):
    for ci, c in enumerate(row):
        if c == "@":
            m[ri, ci] = 1

S = 0
# lvl 1
for ri, row in enumerate(rows):
    for ci, c in enumerate(row):
        if m[ri, ci]:
            subsection = m[max(0,ri-1):min(ri+1+1, len(rows)), max(0, ci-1): min(ci+1+1, len(rows[0]))]

            if np.sum(subsection) <= 4:
                S +=1
                # print(ri, ci, np.sum(subsection)-1 )

print(S)

# lvl 2
SS = 0
S = -1
while S:
    nm = m.copy()
    S = 0
    for ri, row in enumerate(rows):
        for ci, c in enumerate(row):
            if m[ri, ci]:
                subsection = m[max(0,ri-1):min(ri+1+1, len(rows)), max(0, ci-1): min(ci+1+1, len(rows[0]))]

                if np.sum(subsection) <= 4:
                    S +=1
                    nm[ri, ci] = 0
                    # print(ri, ci, np.sum(subsection)-1 )
    m = nm
    SS += S
print(SS)