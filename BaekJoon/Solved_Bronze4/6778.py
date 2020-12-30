# Which Alien?

"""
2020-12-30 오후 4:44
안영준

문제
Canada Cosmos Control은 또 다른 사건에 대한보고를 받았습니다.
그들은 외계인이 불법적으로 우리 공간에 들어갔다고 믿습니다.

최소 3 개의 안테나와 최대 4 개의 눈을 가진 TroyMartian;
최대 6 개의 안테나와 최소 2 개의 눈을 가진 VladSaturnian;
최대 2 개의 안테나와 최대 3 개의 눈을 가진 GraemeMercurian.
입력
첫 번째 줄에는 증인이 외계인을 봤다고 주장한 안테나 수가 포함되어 있습니다. 두 번째 줄에는 외계인에게 보이는 눈의 수가 포함됩니다.

출력
출력은 증인이 제공 한 가능한 설명과 일치하는 외계인 목록입니다. 설명과 일치하는 외계인이 없으면 출력이 없습니다.

"""
ann = int(input())
eyes = int(input())

if ann >= 3 and eyes <= 4:
    print('TroyMartian')

if ann <= 6 and eyes >= 2:
    print('VladSaturnian')

if ann <= 2 and eyes <= 3:
    print('GraemeMercurian')
