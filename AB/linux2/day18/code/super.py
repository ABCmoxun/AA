# super.py


# 此示例示意用super函数访问父类的覆盖方法
class A:
    def work(self):
        print("A类的work方法被调用")

class B(A):
    def work(self):
        print("B类的work方法被调用")

    def doworks(self):
        # self.work()  # 调用B类的
        super(B, self).work()  # 调用超类的方法
        super().work()  # 一样会调用超类的方法
        # super(__class__, self).work()

b = B()
b.work()  # B类的work方法被调用
print("-----以下用b调用覆盖版本的方法----")
# A.work(b)  # A类的work方法被调用
super(B, b).work()
b.doworks()





