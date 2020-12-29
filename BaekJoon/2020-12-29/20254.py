# Site Score

"""
2020-12-29-23 오전 11:48
안영준

2020 Taipei-Hsinchu 지역 대회의 현장 점수는 56U R + 24T R + 14U O + 6T O 입니다.
2020 Taipei-Hsinchu 지역 대회의 사이트 점수를 계산하는 프로그램을 작성하십시오.

입력
입력은 4 빈 분리 된 양의 정수 U 함유 한 줄 갖는 R , T R , U O 및 T O를 .

출력
2020 Taipei-Hsinchu 지역 대회의 현장 점수를 출력합니다.

"""

Ur, Tr, Uo, To = map(int, input().split())
print(56 * Ur + 24 * Tr + 14 * Uo + 6 * To)
