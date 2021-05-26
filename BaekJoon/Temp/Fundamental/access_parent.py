class A:
    def fn(self):
        # 부모클래스에서 아무것도 하지 않을때는
        # pass라는 키워드를 반드시 써야한다.
        pass


class B(A):
    def fn(self):
        print('B')


class C(A):
    def fn(self):
        print('C')


b = B()  # B
c = C()  # C

b.fn()
c.fn()

t = "Hello Python"
k = t[0:3]
l = t[-4:-1]

print(k + l)
