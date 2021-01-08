# 소트인사이드

"""
2021-01-03 오후 7:46
안영준

문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

입력
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

"""

a = input()
number = list()

for i in range(len(a)):
    number.append(int(a[i]))

number.sort(reverse=True)

for i in range(len(a)):
    print(number.__getitem__(i), end='')
