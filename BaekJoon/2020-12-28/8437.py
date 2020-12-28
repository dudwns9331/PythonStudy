# Julka

"""
2020-12-28-19
안영준

두 사람이 정해진 수의 사과의 개수를 가지고 있다.

입력
두 사람이 가진 총 사과의 개수
두 사람이 가진 사과의 차이

출력
두 사람이 각각 가진 사과의 개수

"""

apple = int(input())
diff = int(input())

a = (apple + diff) // 2
b = (apple - diff) // 2

print(a)
print(b)
