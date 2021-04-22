MyList = list(map(int, input().split()))

count = [0] * 11
del MyList[MyList.index(0)]

while MyList:
    count[MyList.pop(0) // 10] += 1

for now in range(10, -1, -1):
    if count[now]:
        print("$%d : %d person" % ((now * 10), count[now]))
