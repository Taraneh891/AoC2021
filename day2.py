d = {}
dep = 0
pos = 0
with open("day2.txt") as f:
    for line in f:
       (key, val) = line.split()
       if (key == 'forward'): pos = pos + int(val)
       if (key == 'down') : dep = dep + int(val)
       if (key == 'up') : dep = dep - int(val)
print(dep * pos)