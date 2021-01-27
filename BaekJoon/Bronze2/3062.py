# 수 뒤집기

"""
2021-01-25 오전 2:04
안영준

문제
수 124를 뒤집으면 421이 되고 이 두 수를 합하면 545가 된다.
124와 같이 원래 수와 뒤집은 수를 합한 수가 좌우 대칭이 되는지 테스트 하는 프로그램을 작성하시오.

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄에 하나의 정수 N(10 ≤ N ≤ 100000)이 주어진다.

출력
각 테스트 케이스에 대해서 원래 수와 뒤집은 수를 합한 수가 좌우 대칭이 되면 YES를 아니면 NO를 한 줄에 하나씩 출력한다.

"""

T = int(input())

result = list()
temp = list()

for i in range(T):
    string = list(map(int, input()))
    temp1 = int(''.join(map(str, string)))
    string.reverse()
    temp2 = int(''.join(map(str, string)))

    for j in range(len(str(temp1 + temp2))):
        result.append(str(temp1 + temp2)[j])
        temp.append(str(temp1 + temp2)[j])
    result.reverse()

    if result == temp:
        print("YES")
    else:
        print("NO")
        
    result.clear()
    temp.clear()