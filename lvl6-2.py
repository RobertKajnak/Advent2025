import numpy as np                  
S= 0
rows = []
with open("lvl6-1.txt", "r") as f:

    for line in f.readlines():
        rows.append(line.strip("\n"))

operators = rows[-1].split()
rows = rows[:-1]

def block_to_number(rows, column_idx, i):
    numbers = []
    for j in range(column_idx, i):
        number = ""
        for row in rows:
            number += row[j]
        # print(number)
        if not number.replace(" ", ""):
            continue
        numbers.append(int(number))
    return numbers

column_idx = 0
numbers = []
for i in range(len(rows[0])):
    for row in rows:
        if row[i] != " ":
            break
    else:
        numbers.append(block_to_number(rows, column_idx, i))
        # print()
        column_idx = i

numbers.append(block_to_number(rows, column_idx, len(rows[0])))


#########


S = 0
for idx, operator in enumerate(operators):
    partial = 0 if operator == "+" else 1
    for number in numbers[idx]:
        partial = (partial + number) if operator == "+" else (partial * number)
    S += partial

print(S)