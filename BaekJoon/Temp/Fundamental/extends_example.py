class A:
    def fn(self):
        # self는 클래스를 수행하면서 기본적으로 인자를 주고받기 때문에
        # self 인자를 넣어준다.
        # self 인자는 넣어주지 않아도 오류는 나지 않는다.
        # 객체를 생성해서 사용하면 기본적으로 넘어가는 인수가 있기 때문에 오류가 난다.
        # self를 통해서 자동적으로 파이썬이 추가해준다.
        print('A')


class B(A):  # 상속은 자식클래스(부모클래스)로 한다.
    def fn(self):
        super().fn()
        print('B')


a = B()

a.fn()
