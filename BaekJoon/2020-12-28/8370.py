#Plane

"""
2020-12-28-17
안영준

문제
Byteland Airlines는 최근 새로운 비행기 모델로 항공기를 확장했습니다.
로운 인수에는  비즈니스 클래스에 n 1 열의 좌석  이 있고 경제 클래스에 n 2 열이 있습니다.
비즈니스 클래스의 각 행에는 k 1 개의  좌석이 있고 경제 클래스의 각 열에는 k 2 개의  좌석이 있습니다.
다음과 같은 프로그램을 작성하십시오.
비행기에서 사용 가능한 좌석에 대한 정보를 읽습니다.
해당 비행기에서 사용 가능한 모든 좌석의 합계를 계산합니다.
결과를 씁니다.

입력
표준 입력의 첫 번째이자 유일한 줄에는 단일 공백으로 구분 된
4개의 정수 n 1 ,  k 1 ,  n 2  및  k 2  (1 ≤ n 1 ,  k 1 ,  n 2 ,  k 2 ≤ 1,000)가 있습니다.

출력
표준 출력의 첫 번째 및 유일한 줄에는 하나의 정수 (비행기에서 사용할 수있는 총 좌석 수)가 포함되어야합니다.

"""

a, b, c, d = map(int, input().split())
print(a*b + c*d)
