# Sounds fishy!

"""
2020-12-30 오후 4:30
안영준

4 개의 입력값을 받아서

증가하는 값이면 Fish Rising.
감소하는 값이면 Fish Diving.
동일한 값이면 Fish At Constant Depth.
아무런 값도 아니면 No Fish.

"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < b < c < d:
    print('Fish Rising')
elif a > b > c > d:
    print('Fish Diving')
elif a == b == c == d:
    print('Fish At Constant Depth')
else:
    print('No Fish')
