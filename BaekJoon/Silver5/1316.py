# 그룹 단어 체커

"""
2021-01-02 오후 4:56
안영준

문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.

리스트, 문자열 공부하고 다시 풀자!

블로그 참조. 숏코딩 -> word.find로 찾은 문자열을 앞으로 당겨서 정렬한다.
정렬된게 나왔던 문자면 원래의 문자열과 다르기 때문에 그룹단어가 아니다.

"""

result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)
