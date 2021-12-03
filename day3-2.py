from collections import Counter


with open("day3.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

oxygen_lines = lines
co_lines = lines

for i in range(0, len(oxygen_lines[0])):
    most_common = Counter(x[i] for x in oxygen_lines).most_common()[0][0]
    if (Counter(x[i] for x in lines).most_common()[0][1] == Counter(x[i] for x in oxygen_lines).most_common()[1][1]): most_common = 1
    oxygen_lines = [l for l in oxygen_lines if l[i] == most_common]
    if len(oxygen_lines) == 1: break
print(oxygen_lines)


for i in range(0, len(co_lines[0])):
    most_common = Counter(x[i] for x in co_lines).most_common()[-1][0]
    if (Counter(x[i] for x in lines).most_common()[-1][1] == Counter(x[i] for x in co_lines).most_common()[-2][1]): most_common = 0
    co_lines = [l for l in co_lines if l[i] == most_common]
    if len(co_lines) == 1: break
print(co_lines)

print(int(oxygen_lines[0],2) * int(co_lines[0],2))
