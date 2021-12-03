from collections import Counter


with open("day3.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

print(lines[0])
gamma = ""
for i in range(0, len(lines[0])):
    most_common = Counter(x[i] for x in lines).most_common()[0][0]
    gamma += most_common

# Because I don't know how NOT binary in Python 
epsilon = gamma.replace("1","2").replace("0","1").replace("2","0")

print(int(gamma,2) * int(epsilon,2))
