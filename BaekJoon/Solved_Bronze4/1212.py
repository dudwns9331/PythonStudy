# 8진수 2진수

"""
2020-12-29 오후 1:34
안영준

문제
8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.

입력
첫째 줄에 8진수가 주어진다. 주어지는 수의 길이는 333,334을 넘지 않는다.

출력
첫째 줄에 주어진 수를 2진수로 변환하여 출력한다. 수가 0인 경우를 제외하고는 반드시 1로 시작해야 한다.

"""

dec_value = int(input(), 8)  # int(값, 진수) 를쓰면 해당 진수로 값을 읽고 10진수로 변환시켜 출력한다.
bin_value = format(dec_value, 'b')  # format '진수 알파벳' 을 통해서 온전한 값을 얻는다.
print(bin_value)