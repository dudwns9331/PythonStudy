# 한수

"""
2021-02-21 오후 1:06
안영준

문제 : https://www.acmicpc.net/problem/1065

"""

number = int(input())
result = 0

for n in range(1, number + 1):
    if n <= 99:
        result += 1
    else:
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            result += 1

print(result)
