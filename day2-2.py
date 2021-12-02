dep = 0
pos = 0
aim = 0
with open("day2.txt") as f:
    for line in f:
       (key, val) = line.split()
       x = int(val)
       if (key == 'forward'): 
           pos = pos + x
           dep = dep + (aim * x)
       if (key == 'down') : aim = aim + x
       if (key == 'up') : aim = aim - x
print(dep * pos)