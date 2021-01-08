# 17 배

"""
2020-12-30 오후 4:00
안영준

문제
상근이는 이진수 곱셈에 어려움을 겪는 여자친구를 위한 프로그램을 만들려고 한다.
상근이의 여자친구는 항상 이진수에 17을 곱한다.
즉, 이진수 N이 입력으로 들어오면 17을 곱한 다음 이진수로 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 이진수 N이 주어진다. N은 최대 1000자리인 이진수이며, 0이 들어오는 경우는 없다.

출력
입력으로 주어진 N을 17배한 다음, 이진수로 출력한다.

"""

bin_value = int(input(), 2)
result = format(bin_value * 17, 'b')
print(result)
