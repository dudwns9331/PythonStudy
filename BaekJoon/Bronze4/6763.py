# Speed fines are not fine!

"""
2020-12-30 오후 4:14
안영준

자동차의 속도에 따라서 벌금을 부여한다.

1~20 -> 100
21 ~ 30 -> 270
31 이상 -> 500

제한 속도를 넘지 않으면  Congratulations, you are within the speed limit! 를 출력한다.

입력
첫째줄에는 제한속도를 입력한다.
두번째 줄에는 운전자의 속도를 입력한다.

출력
제한 속도를 넘지 않으면 Congratulations, you are within the speed limit!
제한속도를 넘으면 You are speeding and your fine is $F. 를 출력한다.

"""

limit = int(input())
speed = int(input())
promising = speed - limit

if promising <= 0:
    print('Congratulations, you are within the speed limit!')
elif 1 <= promising <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= promising <= 30:
    print("You are speeding and your fine is $270.")
elif promising >= 31:
    print("You are speeding and your fine is $500.")
