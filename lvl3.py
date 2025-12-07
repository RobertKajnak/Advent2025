
def find_best(numbers, level):
    if level == 0:
         return []
    
    for first in range(9, 0, -1):
        try:
            mi = numbers.index(first)
        except ValueError:
            continue
        else:
            if (found := find_best(numbers[mi+1:],level-1)) is not False:
                return [first] + found
                
    else:
        return False
    
                         
S= 0
with open("lvl3-1.txt", "r") as f:

    for line in f.readlines():
        numbers = [int(n) for n in line.strip()]
        acc = find_best(numbers, 12)
        print(acc)
        S += sum(v*10**i for i, v in enumerate(acc[::-1]))
print(S)