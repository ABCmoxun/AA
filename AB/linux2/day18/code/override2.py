# override.py


#　当覆盖发生时，子类对象能否调用父类中的方法？
class A:
    def work(self):
        print("A类的work方法被调用")


class B(A):
    def work(self):
        print("B类的work方法被调用")


b = B()
b.work()  # B类的work方法被调用
A.work(b)  # A类的work方法被调用
