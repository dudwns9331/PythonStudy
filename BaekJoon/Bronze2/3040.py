# 백설 공주와 일곱 난쟁이

"""
2021-01-21 오후 4:43
안영준

일곱 난쟁이 문제

"""

result = list()
for i in range(9):
    result.append(int(input()))

total = sum(result)

for i in range(8):
    for j in range(i + 1, 9):
        if total - (result[i] + result[j]) == 100:
            a = result[i]
            b = result[j]

result.remove(a)
result.remove(b)

print('\n'.join(map(str, result)))
