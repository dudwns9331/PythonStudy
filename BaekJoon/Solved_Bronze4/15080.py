# Every Second Counts

"""
2021-01-03 오후 5:14
안영준

문제
Meredith는 Pennsylvania 서부의 작은 마을에있는 고객에게 차량을 제공하는 Ruber라는 택시 서비스를 운영합니다.
그녀는 택시를 이용하는 사람들로부터 가능한 모든 돈을 얻기를 원하기 때문에 그녀의 운전자는 분당이 아닌 초당
고정 요금을 부과합니다. 따라서 고객이 택시에 탑승 한 순간부터 출발하는 순간까지의 정확한 경과 시간을 파악할
수 있어야합니다. 이 작업을 수행하는 프로그램을 작성하려는 시도는 Meredith를 미치게 만들었고 (의도 된 말장난)
그녀가 도움을 청했습니다.

입력
입력은 두 줄로 구성됩니다. 첫 번째 줄에는 시작 시간이 포함되고
두 번째 줄에는 단일 택시 탑승에 대한 종료 시간이 포함됩니다.
각 시간은시, 분 및 초를 제공하는 hh : mm : ss 형식입니다.
Meredith는 24 시간 시계를 사용하며 0 : 0 : 0은 12시 자정을 나타내고 23:59:59는 자정 1 초 전을 나타냅니다.
주행이 자정에 걸쳐있는 경우 종료 시간은 시작 시간 값보다 작은 값을 가질 수 있습니다 (이에 대한 예는 마지막 샘플 테스트 사례 참조).

출력
두 시간 사이의 시간 (초)을 표시합니다. 24 시간 이상의 택시 탑승은 없습니다.

"""

start = input()
end = input()

start_time = start.split(" : ")
end_time = end.split(" : ")

start_time_sec = int(start_time[0]) * 3600 + int(start_time[1]) * 60 + int(start_time[2])
end_time_sec = int(end_time[0]) * 3600 + int(end_time[1]) * 60 + int(end_time[2])

if end_time_sec >= start_time_sec:
    result = end_time_sec - start_time_sec
else:
    result = (end_time_sec + 86400) - start_time_sec

print(result)
