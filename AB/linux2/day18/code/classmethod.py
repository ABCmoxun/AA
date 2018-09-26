# classmethod.py


class A:
    v = 0  # 类变量
    @classmethod
    def get_v(cls):  # 此方法不是实例方法，是类方法
        return cls.v

    @classmethod
    def set_v(cls, value):
        cls.v = value

print(A.get_v())  # 0
A.v = 1
print(A.get_v())  # 1
A.set_v(100)
print(A.get_v())  # 100

a = A()  # 创建一个实例
a.set_v(200)
print(A.get_v())  # 200


