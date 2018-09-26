from day3.tool import my_print


class A:
    def test1(self,n):
        my_print(n)

    def test2(self,m):
        my_print(m)

class B:
    def test3(self,n):
        my_print(n)

    def test4(self,m):
        my_print(m)

a = A()
a.test1(5)
a.test2(8)
b = B()
b.test3(3)
b.test4(4)