import numpy as np                  
S= 0
rows = []
with open("lvl6-1.txt", "r") as f:

    for line in f.readlines():
        rows.append(line.strip().split())
for idx in range(len(rows)-1):
    rows[idx] = [int(e) for e in rows[idx]]


S = 0
for idx, operator in enumerate(rows[-1]):
    partial = 0 if operator == "+" else 1
    for row in rows[:-1]:
        partial = (partial + row[idx]) if operator == "+" else (partial * row[idx])
    S += partial

print(S)