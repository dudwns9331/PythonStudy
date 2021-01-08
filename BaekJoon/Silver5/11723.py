# 집합

"""
2021-01-06 오후 10:36
안영준

문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.

시간 초과?

"""
N = int(input())

result = list()
count = 0


def cal(func, num):
    global result

    if func == 'add':
        if num not in result:
            result.append(num)
    elif func == 'remove':
        if num in result:
            result.remove(num)
    elif func == 'check':
        if num in result:
            print(1)
        else:
            print(0)
    elif func == 'toggle':
        if num in result:
            result.remove(num)
        else:
            result.append(num)
    elif func == 'all':
        result.clear()
        result = [str(i) for i in range(1, 21)]
    elif func == 'empty':
        result.clear()


while count < N:
    func = input().strip()
    count += 1
    count += 1
    if func == 'all' or func == 'empty':
        cal(func, 0)
        continue
    func = func.split()
    cal(func[0], func[1])
