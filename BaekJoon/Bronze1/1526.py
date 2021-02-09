# 가장 큰 금민수

"""
2021-02-03 오전 9:00
안영준

문제
은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.
N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 4보다 크거나 같고 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 N보다 작거나 같은 금민수 중 가장 큰 것을 출력한다.

"""

n = int(input())

result_list = list()

for i in range(4, n + 1):
    is_ok = True
    result = str(i)
    for j in range(len(result)):
        if result[j] != '4' and result[j] != '7':
            is_ok = False
            break
    if is_ok:
        result_list.append(result)

print(result_list[-1])
