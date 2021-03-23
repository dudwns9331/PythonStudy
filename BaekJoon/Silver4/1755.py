# 숫자놀이

"""
2021-03-22 오후 3:27
안영준

문제 : https://www.acmicpc.net/problem/1755
"""

number = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
          "8": "eight", "9": "nine"}

M, N = map(int, input().split())

number_list = [str(i) for i in range(M, N + 1)]

string_number = dict()
temp_number = dict()
count = 0

number_seq = list()

for i in number_list:
    string = ""
    for j in range(len(i)):
        if i[j] in number:
            string = string + number.get(i[j])
    string_number.__setitem__(string, count)
    count += 1

temp_number = string_number

string_number = sorted(string_number)

for i in string_number:
    number_seq.append(temp_number.get(i))

count = 0
for i in number_seq:
    print(number_list[i], end=" ")
    count += 1
    if count % 10 == 0:
        print()
        count = 0
