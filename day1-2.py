try:
    list = []
    while True:
        list.append(int(input()))
except:
    len = len(list)
    r = 0
    for i in range(len):
        if (
            (i > 1)
            and (i < (len - 1))
            and (
                list[i - 2] + list[i - 1] + list[i]
                < list[i - 1] + list[i] + list[i + 1]
            )
        ):
            r = r + 1
    print(r)
