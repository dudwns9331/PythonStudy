# 알파벳 전부 쓰기

"""
2021-02-08 오전 9:44
안영준

문제
팬그램은 26개의 알파벳, a~z를 최소 한번씩 모두 사용한 문장을 말한다. 아마 가장 유명한
문장은 이것일 것이다. "The quick brown fox jumps over the lazy dog."
꿍은 다른 문장들중에 팬그램인 것은 없는지 궁금해졌다. 그래서 여러분이 할 일은 꿍을
위해 어떠한 문장이 팬그램인지 아닌지를 판별해주는 프로그램을 짜는 것이다.
팬그램에서는 알파벳의 대소문자를 구분하지 않는다고 하자.

입력
입력의 첫 번째 줄은 1 ≤ N ≤ 50의 N이 주어진다.
다음 N개의 줄은 각각 한 문장이 주어지는데, 알파벳의 대소문자, 공백, 숫자, 그리고 분장부호들(. , ? ! ' ")이 포함될 수 있다.
각 문장은 최소 한개의 문자를 포함하며 100개를 넘지는 않는다.

출력
각 입력에 대해, 팬그램에 해당하면 "pangram"을 출력한다.
만약 팬그램이 아닐 경우, "missing"을 출력한 후 한칸 띄고 문장에 나타나지 않은
문자들을 모두 출력한다. 이때, 나타나지 않은 문자들은 모두 소문자로 출력하며 알파벳 순서대로 정렬된상태로 출력해야 한다.

"""

n = int(input())

for i in range(n):
    string = input().lower()
    result = list()
    answer = list()
    alp = [chr(i).lower() for i in range(65, 91)]
    for j in string:
        if j in alp:
            result.append(j)
    result = set(result)
    result = list(result)
    result.sort()

    if result != alp:
        for j in result:
            if j in alp:
                alp.remove(j)
        print('missing ' + ''.join(map(str, alp)))
    else:
        print('pangram')
