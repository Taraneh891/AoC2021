try:
    list = []
    while True:
        list.append(int(input()))
except:
    print("ok")
    len = len(list)
    print(len)
    r = 0
    for i in range(len):
        if list[i - 1] < list[i]:
            r = r + 1
    print(r)
